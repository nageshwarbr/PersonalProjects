# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time


def isNowInTimePeriod(start_time, end_time, now_time):
    return start_time <= now_time <= end_time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")


if __name__ == '__main__':

    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40 * 60
    exsecs = 30 * 60
    eyesecs = 45 * 60

    timeStart = '9:00AM'
    timeEnd = '5:00PM'
    timeEnd = datetime.strptime(timeEnd, "%I:%M%p")
    timeStart = datetime.strptime(timeStart, "%I:%M%p")
    timeNow = datetime.now()

    while isNowInTimePeriod(timeStart, timeEnd, datetime.now()):
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop alarm")
            musiconloop("water.mp3", "drank")
            init_water = time()
            log_now("Drank water at ")
        if time() - init_eyes > eyesecs:
            print("Eye drop time. Enter 'doneeyes' to stop alarm")
            musiconloop("eyes.mp3", "doneeyes")
            init_eyes = time()
            log_now("Eye drop  at ")
        if time() - init_exercise > exsecs:
            print("Exercise time. Enter 'done' to stop alarm")
            musiconloop("exercise.mp3", "done")
            init_exercise = time()
            log_now(" Exercise at ")
