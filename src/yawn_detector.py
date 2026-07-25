import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "Models" / "CNN_Yawn_classifier.tflite"

interpreter = tflite.Interpreter(
    model_path=str(MODEL_PATH)
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


YAWN_SCORE_THRESHOLD = 0.37
MOUTH_RATIO_THRESHOLD = 0.25


def mouth_aspect_ratio(mouth_coordinates):
    x1, y1, x2, y2 = mouth_coordinates
    width = max(1.0, float(x2 - x1))
    height = max(1.0, float(y2 - y1))
    return height / width


def yawn_detection(mouth_frame, mouth_coordinates=None):
    mouth_frame = cv2.cvtColor(mouth_frame, cv2.COLOR_BGR2RGB)
    mouth_frame = cv2.resize(mouth_frame, (128, 128))
    mouth_frame = mouth_frame.astype(np.float32) / 255.0
    mouth_frame = np.expand_dims(mouth_frame, axis=0)

    interpreter.set_tensor(input_details[0]["index"], mouth_frame)
    interpreter.invoke()

    prediction = float(interpreter.get_tensor(output_details[0]["index"])[0][0])
    mouth_ratio = mouth_aspect_ratio(mouth_coordinates) if mouth_coordinates is not None else None

    score_status = 1 if prediction > YAWN_SCORE_THRESHOLD else 0
    ratio_status = 1 if mouth_ratio is not None and mouth_ratio > MOUTH_RATIO_THRESHOLD else 0
    status = 1 if score_status == 1 or ratio_status == 1 else 0

    print(
        "Yawn Score:", prediction,
        "Mouth ratio:", mouth_ratio,
        "Status:", status,
    )

    return status, prediction, mouth_ratio