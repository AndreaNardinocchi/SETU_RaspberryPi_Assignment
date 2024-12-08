#!/bin/python3
# https://projects.raspberrypi.org/en/projects/countdown-timer/4

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]
R = [255, 0, 0]
X = [0, 0, 0]

s = 7200

timer = []



for i in range(64):
  if i <= 64:
    timer.append(G)
  else:
    timer.append(X)

sense.set_pixels(timer)

for i in range(0, s):
  sleep(1)
  timer[i]=R 

  sense.set_pixels(timer)
