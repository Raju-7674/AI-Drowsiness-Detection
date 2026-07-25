from src.dlib_detector import detect_landmarks
from src.preprocessing import preprocess_frame
from src.eye_detector import eye_closure_detection
from src.yawn_detector import yawn_detection
from src.alarm import check_drowsiness
import base64
from pathlib import Path
import streamlit as st
import numpy as np
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import streamlit.components.v1 as components
import av
import cv2
from collections import deque
import os


@st.cache_data(show_spinner=False)
def load_alarm_audio_b64():
    alarm_path = Path(__file__).resolve().parent / "alarm.mp3"
    return base64.b64encode(alarm_path.read_bytes()).decode("utf-8")


def render_alarm_audio():
    audio_b64 = load_alarm_audio_b64()
    components.html(
        f"""
        <audio id="drowsy-alarm" preload="auto" loop>
            <source src="data:audio/mpeg;base64,{audio_b64}" type="audio/mpeg">
        </audio>
        <script>
            const alarm = document.getElementById('drowsy-alarm');
            if (alarm) {{
                alarm.loop = true;
                alarm.play().catch(() => {{}});
            }}
        </script>
        """,
        height=0,
        scrolling=False,
    )


class DrowsinessDetector(VideoTransformerBase):
    def __init__(self):
        self.eye_status = None
        self.eye_left = None
        self.eye_right = None
        self.yawn_status = None
        self.yawn_score = None
        self.mouth_ratio = None
        self.yawn_scores = deque(maxlen=7)
        self.mouth_ratios = deque(maxlen=7)
        self.eye_closed_probs = deque(maxlen=7)
        self.smoothed_eye_status = None
        self.smoothed_yawn_status = None
        self.alarm = False

    def recv(self, frame):
        frame = frame.to_ndarray(format="bgr24")
        frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a mirror effect

        try:
            res = detect_landmarks(frame)
            if len(res) == 6:
                frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates, left_ear, right_ear = res
            else:
                frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates = res
                left_ear = None
                right_ear = None
            print("Landmarks:", left_eye_coordinates, right_eye_coordinates, mouth_coordinates, "EARs:", left_ear, right_ear)

        # No face detected -> just return the current frame
            if (
                left_eye_coordinates is None
                or right_eye_coordinates is None
                or mouth_coordinates is None
            ):
                self.eye_status = None
                self.yawn_status = None
                self.alarm = False
                return av.VideoFrame.from_ndarray(frame, format="bgr24")

            left_eye_frame, right_eye_frame, mouth_frame = preprocess_frame(
                frame,
                left_eye_coordinates,
                right_eye_coordinates,
                mouth_coordinates,
            )

            if left_eye_frame is not None and right_eye_frame is not None:
                print('Eye frames:', left_eye_frame.shape, right_eye_frame.shape)
                try:
                    self.eye_status, self.eye_left, self.eye_right, left_raw, right_raw = eye_closure_detection(left_eye_frame, right_eye_frame)
                    left_closed_prob = float(left_raw[0]) if len(left_raw) > 0 else 0.0
                    right_closed_prob = float(right_raw[0]) if len(right_raw) > 0 else 0.0
                    mean_closed = (left_closed_prob + right_closed_prob) / 2.0
                    self.eye_closed_probs.append(mean_closed)
                    mean_closed_smoothed = sum(self.eye_closed_probs) / len(self.eye_closed_probs)
                    # EAR fallback: eyes closed if both EARs are below threshold
                    EAR_THRESHOLD = 0.20
                    ear_closed = False
                    if left_ear is not None and right_ear is not None:
                        ear_closed = (left_ear < EAR_THRESHOLD and right_ear < EAR_THRESHOLD)
                    self.smoothed_eye_status = 1 if (mean_closed_smoothed > 0.5 or ear_closed) else 0
                    print("Eye Status:", self.eye_status, "Left/Right:", self.eye_left, self.eye_right, left_raw, right_raw, "smoothed:", self.smoothed_eye_status)
                except Exception as e:
                    print("Eye inference error:", e)
                    self.eye_status = None
                    self.eye_left = None
                    self.eye_right = None
                # save debug crops for inspection (limited)
                try:
                    dbg_dir = Path(__file__).resolve().parent.parent / 'debug'
                    os.makedirs(dbg_dir, exist_ok=True)
                    # rotate index based on existing files
                    existing = len(list(dbg_dir.glob('left_*.png')))
                    if existing < 10:
                        left_path = dbg_dir / f'left_{existing}.png'
                        right_path = dbg_dir / f'right_{existing}.png'
                        cv2.imwrite(str(left_path), left_eye_frame)
                        cv2.imwrite(str(right_path), right_eye_frame)
                except Exception as _:
                    pass
            else:
                print('Eye crop invalid or missing')
                self.eye_status = None
                self.eye_left = None
                self.eye_right = None

            if mouth_frame is not None:
                print('Mouth frame:', mouth_frame.shape)
                try:
                    self.yawn_status, self.yawn_score, self.mouth_ratio = yawn_detection(mouth_frame, mouth_coordinates)
                    # temporal smoothing
                    if self.yawn_score is not None:
                        self.yawn_scores.append(self.yawn_score)
                    if self.mouth_ratio is not None:
                        self.mouth_ratios.append(self.mouth_ratio)
                    mean_score = sum(self.yawn_scores) / len(self.yawn_scores) if len(self.yawn_scores) > 0 else 0.0
                    mean_ratio = sum(self.mouth_ratios) / len(self.mouth_ratios) if len(self.mouth_ratios) > 0 else None
                    # Decision rule:
                    # - If model score is very high, flag yawn
                    # - Else if model score is moderately high AND mouth ratio indicates openness, flag yawn
                    # - Otherwise, do not flag
                    if mean_score > 0.45:
                        smoothed_yawn = 1
                    elif mean_score > 0.37 and (mean_ratio is not None and mean_ratio > 0.20):
                        smoothed_yawn = 1
                    else:
                        smoothed_yawn = 0
                    self.smoothed_yawn_status = smoothed_yawn
                    print("Yawn Status:", self.yawn_status, "Score:", self.yawn_score, "Ratio:", self.mouth_ratio, "smoothed:", self.smoothed_yawn_status)
                except Exception as e:
                    print("Yawn inference error:", e)
                    self.yawn_status = None
                    self.yawn_score = None
                    self.mouth_ratio = None
            else:
                print('Mouth crop invalid or missing')
                self.yawn_status = None
                self.yawn_score = None
                self.mouth_ratio = None

            # use smoothed statuses for alarm
            use_eye = self.smoothed_eye_status if self.smoothed_eye_status is not None else self.eye_status
            use_yawn = self.smoothed_yawn_status if self.smoothed_yawn_status is not None else self.yawn_status
            self.alarm = check_drowsiness(use_eye, use_yawn)
            print("Alarm:", self.alarm)
        except Exception as e:
            print("Video processing error:", e)

        return av.VideoFrame.from_ndarray(frame, format="bgr24")
def main():
    st.set_page_config(
        page_title="Drowsiness Detection System",
        page_icon="👁️",
        layout="wide",
    )
    # Simple automatic refresh to ensure UI updates without extra clicks.
    # NOTE: This reloads the whole page every 2s (simple but can feel choppy).
    components.html(
        """
        <script>
        setInterval(() => { try { window.location.reload(); } catch(e){} }, 2000);
        </script>
        """,
        height=0,
    )
    if "sound_enabled" not in st.session_state:
        # enable sound by default so alarm can play automatically when detected
        st.session_state.sound_enabled = True

    st.title("Drowsiness Detection System")
    col1, col2 = st.columns([2,1])
    with col1:
        st.subheader("Live Camera Feed")
        ctx=webrtc_streamer(
            key="drowsiness-detector",
            video_processor_factory=DrowsinessDetector,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True
        )
    with col2:
        st.subheader("Drowsiness Status")
        if ctx.video_processor:
            eye_status = ctx.video_processor.smoothed_eye_status if ctx.video_processor.smoothed_eye_status is not None else ctx.video_processor.eye_status
            yawn_status = ctx.video_processor.smoothed_yawn_status if ctx.video_processor.smoothed_yawn_status is not None else ctx.video_processor.yawn_status
            alarm = ctx.video_processor.alarm

            if eye_status is None:
                st.metric(label="Eye Status", value="Face not detected", delta_color="yellow")
            else:
                ear_col = "green" if eye_status == 0 else "red"
                st.metric(label="Eye Status", value="Open" if eye_status == 0 else "Closed", delta_color=ear_col)
                st.caption(f"Eye raw predictions: left={ctx.video_processor.eye_left}, right={ctx.video_processor.eye_right}")

            if yawn_status is None:
                st.metric(label="Yawn Status", value="Face not detected", delta_color="yellow")
            else:
                yawn_col = "green" if yawn_status == 0 else "red"
                st.metric(label="Yawn Status", value="No Yawning" if yawn_status == 0 else "Yawning", delta_color=yawn_col)
                st.caption(f"Yawn score: {ctx.video_processor.yawn_score:.3f}, mouth ratio: {ctx.video_processor.mouth_ratio:.3f}")
                if yawn_status == 1:
                    st.warning("Yawning Detected!")
                else:
                    st.success("No Yawning")

            if eye_status is None or yawn_status is None:
                st.info("Waiting for a clear face/mouth view...")

            # allow user to enable/disable alarm sound
            st.checkbox("Enable warning sound", value=st.session_state.sound_enabled, key="sound_enabled")

            if alarm:
                st.error("⚠️ DROWSINESS DETECTED!")
                if st.session_state.sound_enabled:
                    render_alarm_audio()
            elif st.session_state.sound_enabled:
                st.info("Alarm is armed. It will play as soon as drowsiness is detected.")

if __name__ == '__main__':
    main()