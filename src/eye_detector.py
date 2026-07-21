import tensorflow as tf
import numpy as np
import cv2
def eye_closure_detection(left_eye_frame, right_eye_frame):
    model = tf.keras.models.load_model("/home/nani/Desktop/kanaka raju/Eye_Closure_Detection/Models/CNN_Eye_classifier.keras")
    left_eye_frame = cv2.resize(left_eye_frame, (24, 24))  # Resize to match model input size
    right_eye_frame = cv2.resize(right_eye_frame, (24, 24))
    
    left_eye_frame = left_eye_frame / 255.0  # Normalize pixel values
    right_eye_frame = right_eye_frame / 255.0
    
    # Expand dimensions to match model input shape
    left_eye_frame = np.expand_dims(left_eye_frame, axis=0)
    right_eye_frame = np.expand_dims(right_eye_frame, axis=0)
    
    # Make predictions for both eyes
    left_eye_prediction = model.predict(left_eye_frame)
    right_eye_prediction = model.predict(right_eye_frame)
    left_eye_prediction = np.argmax(left_eye_prediction,axis=1)
    right_eye_prediction = np.argmax(right_eye_prediction,axis=1)
    
    # Determine if eyes are closed based on predictions (assuming binary classification)
    left_eye_open = left_eye_prediction[0][0] > 0.5
    right_eye_open = right_eye_prediction[0][0] > 0.5
    
    return (True if left_eye_open and right_eye_open else False)