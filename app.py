from src.camera import get_frames
import cv2
if __name__ == '__main__':
    for frame in get_frames(0):
        # Process the frame (e.g., display it, save it, etc.)
        cv2.imshow('Camera Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
