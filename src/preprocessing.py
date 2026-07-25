import cv2
import numpy as np

MIN_CROP_SIZE = 20


def _safe_crop(frame, coordinates, padding=20):
    x1, y1, x2, y2 = coordinates
    h, w = frame.shape[:2]
    x1 = max(0, x1 - padding)
    y1 = max(0, y1 - padding)
    x2 = min(w, x2 + padding)
    y2 = min(h, y2 + padding)

    if x2 <= x1 or y2 <= y1:
        return None

    if x2 - x1 < MIN_CROP_SIZE or y2 - y1 < MIN_CROP_SIZE:
        return None

    crop = frame[y1:y2, x1:x2]
    if crop.size == 0:
        return None

    return crop


def preprocess_frame(frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates):
    if left_eye_coordinates is None and right_eye_coordinates is None and mouth_coordinates is None:
        return None, None, None

    left_eye_frame = None
    right_eye_frame = None
    mouth_frame = None

    if left_eye_coordinates is not None and right_eye_coordinates is not None:
        left_eye_frame = _safe_crop(frame, left_eye_coordinates)
        right_eye_frame = _safe_crop(frame, right_eye_coordinates)

    if mouth_coordinates is not None:
        mouth_frame = _safe_crop(frame, mouth_coordinates)

    return left_eye_frame, right_eye_frame, mouth_frame