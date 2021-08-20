from datetime import datetime
from playsound import playsound

alarm_time = input("Enter your time to set alaram HH:MM:SS:")

alarm_hour = alarm_time[0:2]
alarm_minuts = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("setting up alaram")

while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minuts = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    if (alarm_period == current_period):
        if (alarm_hour == current_hour):
            if (alarm_minuts == current_minuts):
                if (alarm_seconds == current_seconds):
                    print("Wake up")
                    playsound("audio.mp3")
                    break