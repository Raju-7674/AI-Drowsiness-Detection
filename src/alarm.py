import pygame
import time
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound('/home/nani/Desktop/kanaka raju/Eye_Closure_Detection/flutie8211-low-pitch-alarm-buzzer-451576.mp3')
sound_playing = False
sound_lock=pygame.mixer
drowsy_start_time=None
def play_alarm():
    global sound_playing
    if not sound_playing:
        alarm_sound.play(-1)  # Play the alarm sound in a loop
        sound_playing = True
def stop_alarm():
    global sound_playing
    if sound_playing:
        alarm_sound.stop()  # Stop the alarm sound
        sound_playing = False
def check_drowsiness(eye_status, yawn_status):
    global drowsy_start_time
    if eye_status == 0 or yawn_status == 1:
        if drowsy_start_time is None:
            drowsy_start_time = time.time()  # Start the timer
        elif time.time() - drowsy_start_time >= 3:  # Check if drowsiness persists for 3 seconds
            play_alarm()
    else:
        stop_alarm()
        drowsy_start_time = None  # Reset the timer when the user is not drowsy
