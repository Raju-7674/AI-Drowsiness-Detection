import tensorflow as tf
import cv2
import numpy as np
def yawn_detection(mouth_frame):
    model = tf.keras.models.load_model("/home/nani/Desktop/kanaka raju/Eye_Closure_Detection/Models/CNN_Yawn_classifier.keras")
    mouth_frame = cv2.resize(mouth_frame, (24, 24))  # Resize to match model input size
    mouth_frame = mouth_frame / 255.0
    mouth_frame = np.expand_dims(mouth_frame, axis=0)
    mouth_prediction = model.predict(mouth_frame)
    mouth_prediction = np.argmax(mouth_prediction, axis=1)
    
    # Determine if the mouth is open based on prediction (assuming binary classification)
    mouth_open = mouth_prediction[0][0] > 0.5
    
    return (True if mouth_open else False)