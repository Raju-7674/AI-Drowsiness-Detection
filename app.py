from src.camera import get_frames
from src.dlib_detector import detect_landmarks
from src.preprocessing import preprocess_frame
import cv2
if __name__ == '__main__':
    for frame in get_frames(0):
        # Process the frame (e.g., display it, save it, etc.)
        frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates = detect_landmarks(frame)
        left_eye_frame, right_eye_frame, mouth_frame= preprocess_frame(frame, left_eye_coordinates, right_eye_coordinates, mouth_coordinates)
        
        cv2.imshow('Camera Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
