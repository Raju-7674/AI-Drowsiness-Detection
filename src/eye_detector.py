import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "Models" / "CNN_Eye_classifier.tflite"

interpreter = tflite.Interpreter(
    model_path=str(MODEL_PATH)
)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def eye_closure_detection(left_eye_frame, right_eye_frame):

    def predict(img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224))
        img = img.astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)

        interpreter.set_tensor(input_details[0]["index"], img)
        interpreter.invoke()

        output = interpreter.get_tensor(output_details[0]["index"])
        print("Raw Output:", output)
        return int(np.argmax(output)), output.flatten().tolist()

    left, left_raw = predict(left_eye_frame)
    right, right_raw = predict(right_eye_frame)

    left_prob_closed = float(left_raw[0]) if len(left_raw) > 0 else 0.0
    right_prob_closed = float(right_raw[0]) if len(right_raw) > 0 else 0.0

    print("Left Prediction:", left, left_raw)
    print("Right Prediction:", right, right_raw)
    print("Left closed prob:", left_prob_closed, "Right closed prob:", right_prob_closed)

    status = 1 if left_prob_closed > 0.5 and right_prob_closed > 0.5 else 0
    print("Eye Status Returned:", status)

    return status, left, right, left_raw, right_raw