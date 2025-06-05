import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Heartbeat.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")
        
        if current_time == alarm_time:
            print("\nAlarm ringing!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play(-1)
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            pygame.mixer.music.stop()
            is_running = False
        time.sleep(1)

    print("Alarm has been stopped.")

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time if alarm_time else "00:00:00")
    print("Alarm time not set, defaulting to 00:00:00.")

