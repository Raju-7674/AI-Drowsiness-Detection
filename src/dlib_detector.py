import dlib
import cv2
import numpy as np
detector = dlib.get_frontal_face_detector()
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "Models" / "shape_predictor_68_face_landmarks.dat"
import os
print("Current Working Directory:", os.getcwd())
print("Model Path:", MODEL_PATH)
print("Exists:", MODEL_PATH.exists())
predictor = dlib.shape_predictor(str(MODEL_PATH))

def detect_landmarks(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        left_eye_top = landmarks.part(37).y
        left_eye_bottom =landmarks.part(41).y
        left_eye_left = landmarks.part(36).x
        left_eye_right = landmarks.part(39).x
        right_eye_top = landmarks.part(43).y
        right_eye_bottom = landmarks.part(47).y
        right_eye_left = landmarks.part(42).x
        right_eye_right = landmarks.part(45).x
        mouth_top = landmarks.part(62).y
        mouth_bottom = landmarks.part(66).y
        mouth_left = landmarks.part(48).x
        mouth_right = landmarks.part(54).x
        left_eye_coordinates = [left_eye_left, left_eye_top, left_eye_right, left_eye_bottom]
        right_eye_coordinates = [right_eye_left, right_eye_top, right_eye_right, right_eye_bottom]
        mouth_coordinates = [mouth_left, mouth_top, mouth_right, mouth_bottom]
        def ear(pts_idx):
            p = [(landmarks.part(i).x, landmarks.part(i).y) for i in pts_idx]
            import math
            A = math.hypot(p[1][0]-p[5][0], p[1][1]-p[5][1])
            B = math.hypot(p[2][0]-p[4][0], p[2][1]-p[4][1])
            C = math.hypot(p[0][0]-p[3][0], p[0][1]-p[3][1])
            if C == 0:
                return 0.0
            return (A + B) / (2.0 * C)
        left_ear = ear([36,37,38,39,40,41])
        right_ear = ear([42,43,44,45,46,47])
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
        return frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates, left_ear, right_ear
    return frame, None, None, None
