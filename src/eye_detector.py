import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

# Load interpreter only once
interpreter = tflite.Interpreter(
    model_path="/home/nani/Desktop/kanaka raju/Eye_Closure_Detection/Models/CNN_Eye_classifier.tflite"
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def eye_closure_detection(left_eye_frame, right_eye_frame):

    def predict(img):
        img = cv2.resize(img, (224, 224))
        img = img.astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)

        interpreter.set_tensor(input_details[0]["index"], img)
        interpreter.invoke()

        output = interpreter.get_tensor(output_details[0]["index"])

        return np.argmax(output)

    left = predict(left_eye_frame)
    right = predict(right_eye_frame)

    return 1 if left == 1 and right == 1 else 0