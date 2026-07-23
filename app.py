from src.dlib_detector import detect_landmarks
from src.preprocessing import preprocess_frame
from src.eye_detector import eye_closure_detection
from src.yawn_detector import yawn_detection
from src.alarm import check_drowsiness
import streamlit as st
import numpy as np
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import av
import cv2
class DrowsinessDetector(VideoTransformerBase):
    def __init__(self):
        self.eye_status = 0
        self.yawn_status = 0

    def recv(self, frame):
        frame = frame.to_ndarray(format="bgr24")
        frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates = detect_landmarks(frame)
        left_eye_frame, right_eye_frame, mouth_frame= preprocess_frame(frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates)
        self.eye_status = eye_closure_detection(left_eye_frame, right_eye_frame)
        self.yawn_status = yawn_detection(mouth_frame)
        check_drowsiness(self.eye_status, self.yawn_status)
        return av.VideoFrame.from_ndarray(frame, format="bgr24")
def main():
    st.set_page_config(
        page_title="Drowsiness Detection System",
        page_icon="👁️",
        layout="wide",
    )
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
            eye_status = ctx.video_processor.eye_status
            yawn_status = ctx.video_processor.yawn_status
            ear_col = "green" if eye_status == 1 else "red"
            st.metric(label="Eye Status", value="Open" if eye_status == 1 else "Closed", delta_color=ear_col)
            yawn_col = "green" if yawn_status == 0 else "red"
            st.metric(label="Yawn Status", value="No Yawning" if yawn_status == 0 else "Yawning", delta_color=yawn_col)
            if yawn_status == 1:
                st.warning("Yawning Detected!")
            else:
                st.success("No Yawning")

if __name__ == '__main__':
    main()