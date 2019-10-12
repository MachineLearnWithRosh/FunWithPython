from pygame import mixer
from datetime import datetime
from time import time


def musicOnloop(filename, stopword):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while True:
        userInput = input()
        if userInput.title() == stopword:
            mixer.music.stop()
            break

def log_activity(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water=time()
    init_eye=time()
    init_phy=time()
    watersecs=5
    eyesecs=10
    exsecs=20

    while True:
        if time()-init_water > watersecs:
            print("Its drinking time. Enter 'Drank' to stop")
            musicOnloop("water.mp3","Drank")
            init_water=time()
            log_activity("Drank water at")

        if time() - init_eye > eyesecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musicOnloop('water.mp3', 'Doneeyes')
            init_eye = time()
            log_activity("Eyes Relaxed at")

        if time() - init_phy > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musicOnloop('physical.mp3', 'Donephy')
            init_phy = time()
            log_activity("Physical Activity done at")
