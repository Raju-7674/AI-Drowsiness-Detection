import time

drowsy_start_time = None


def check_drowsiness(eye_status, yawn_status):
    global drowsy_start_time

    if eye_status == 0 or yawn_status == 1:
        if drowsy_start_time is None:
            drowsy_start_time = time.time()

        elif time.time() - drowsy_start_time >= 3:
            return True

    else:
        drowsy_start_time = None

    return False