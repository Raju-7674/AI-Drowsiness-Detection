import dlib
import cv2
import numpy as np
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/nani/Desktop/kanaka raju/Eye_Closure_Detection/Models/shape_predictor_68_face_landmarks.dat")
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
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
        return frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates
    return frame, None, None, None