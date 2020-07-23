import datetime
from pygame import mixer
from time import time

# for time
def timee():
    return datetime.datetime.now()


def water():
    mixer.init()
    mixer.music.load('water.mp3')
    mixer.music.play(1000, 0.0)

    y = input('Enter Stop after Complete the task : ')
    if y == 'stop':
        mixer.music.pause()
        fb = open('Healthy_Programmer.txt', 'a')
        time_1 = str(timee())
        fb.write(time_1)
        fb.write('\t')
        fb.write(' : Water ')
        fb.write('\n')
        fb.close()


def eye():
    mixer.init()
    mixer.music.load('eye.mp3')
    mixer.music.play(1000, 0.0)
    y = input('Enter Stop After Complete the task : ')
    if y == 'stop':
        mixer.music.pause()
        fb = open('Healthy_Programmer.txt', 'a')
        time_1 = str(timee())
        fb.write(time_1)
        fb.write('\t')
        fb.write(' : Eye Exercise')
        fb.write('\n')
        fb.close()


def physical():
    mixer.init()
    mixer.music.load('physical.mp3')
    mixer.music.play(1000, 0.0)
    y = input('Enter Stop After Complete the Task : ')
    if y == 'stop':
        mixer.music.pause()
        fb = open('Healthy_Programmer.txt', 'a')
        time_1 = str(timee())
        fb.write(time_1)
        fb.write('\t')
        fb.write(' : Physical Exercise ')
        fb.write('\n')
        fb.close()


# at 9 am

water()
eye()
physical()

init_water = time()
init_eye = time()
init_phy = time()

water_sec = 25*60
eye_sec = 30*60
phy_sec = 45*60





while True:
    if time() - init_water > water_sec:
        water()
        init_water = time()

    if time() - init_eye > eye_sec:
        eye()
        init_eye = time()

    if time() - init_phy > phy_sec:
        physical()
        init_phy = time()