import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

# Load the model only once
interpreter = tflite.Interpreter(
    model_path="/home/nani/Desktop/kanaka raju/Eye_Closure_Detection/Models/CNN_Yawn_classifier.tflite"
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def yawn_detection(mouth_frame):

    # Change (224,224) to (128,128) if your model expects 128x128
    mouth_frame = cv2.resize(mouth_frame, (224, 224))

    mouth_frame = mouth_frame.astype(np.float32) / 255.0
    mouth_frame = np.expand_dims(mouth_frame, axis=0)

    interpreter.set_tensor(input_details[0]["index"], mouth_frame)
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]["index"])

    prediction = np.argmax(prediction)

    return 1 if prediction == 1 else 0