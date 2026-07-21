import cv2
import numpy as np
def preprocess_frame(frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates):
    left_eye_img=frame.copy()
    right_eye_img=frame.copy()
    mouth_img=frame.copy()
    if left_eye_coordinates is not None and right_eye_coordinates is not None and mouth_coordinates is not None:
        left_eye_frame = left_eye_img[left_eye_coordinates[1]:left_eye_coordinates[3], left_eye_coordinates[0]:left_eye_coordinates[2]]
        right_eye_frame = right_eye_img[right_eye_coordinates[1]:right_eye_coordinates[3], right_eye_coordinates[0]:right_eye_coordinates[2]]
        mouth_frame = mouth_img[mouth_coordinates[1]:mouth_coordinates[3], mouth_coordinates[0]:mouth_coordinates[2]]
        return left_eye_frame, right_eye_frame, mouth_frame
    else:
        return None, None, None