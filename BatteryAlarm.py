import psutil
import time
from pygame import mixer

# battery_status = psutil.sensors_battery()
# battery_status,_, _ = psutil.sensors_battery()


mixer.init()
mixer.music.load("sample2.mp3")

while True:
    time.sleep(180)
    battery_status, _, _ = psutil.sensors_battery()
    print(battery_status)
    if battery_status >= 98 or battery_status <= 20:
        mixer.music.play()
        time.sleep(5)
        mixer.music.stop()
        # exit()
