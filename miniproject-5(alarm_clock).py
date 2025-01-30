import time
import os
import platform
from datetime import datetime

# For playing sound on Windows
if platform.system() == "Windows":
    import winsound
# For playing sound on macOS/Linux
else:
    from playsound import playsound

def play_ringtone():
    """Play the ringtone."""
    ringtone_path = "alarm_sound.wav"  # Replace with your ringtone file path
    if platform.system() == "Windows":
        winsound.PlaySound(ringtone_path, winsound.SND_FILENAME)
    else:
        playsound(ringtone_path)

def set_alarm(alarm_time):
    """Set the alarm for a specific time."""
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up! Wake up!")
            play_ringtone()
            break
        time.sleep(1)  # Check every second

def set_timer(seconds):
    """Set a timer for a specific number of seconds."""
    print(f"Timer set for {seconds} seconds.")
    time.sleep(seconds)
    print("Timer is up!")
    play_ringtone()

def main():
    print("Welcome to the Python Alarm Clock!")
    choice = input("Do you want to set an alarm or a timer? (alarm/timer): ").strip().lower()

    if choice == "alarm":
        alarm_time = input("Enter the alarm time in HH:MM:SS format (e.g., 07:30:00): ").strip()
        set_alarm(alarm_time)
    elif choice == "timer":
        try:
            seconds = int(input("Enter the timer duration in seconds: ").strip())
            set_timer(seconds)
        except ValueError:
            print("Invalid input. Please enter a valid number of seconds.")
    else:
        print("Invalid choice. Please choose 'alarm' or 'timer'.")

if __name__ == "__main__":
    main()