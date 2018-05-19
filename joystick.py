#!/usr/bin/python3
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

import time
import datetime
import math
import numled

from sense_hat import SenseHat
sense = SenseHat()

colors = [(255, 0, 0), (255, 255, 255)]
cancelled = False
was_cancelled = False

def pushed(event):
    global cancelled
    global was_cancelled
    if event.action != ACTION_RELEASED:
        cancelled = True
        was_cancelled = True
        time.sleep(1)
        numled.show_number(sense, 10, colors[0])
        time.sleep(.5)
        numled.show_number(sense, 10, colors[1])
        time.sleep(.5)
        sense.clear()
            
def warn():
    global cancelled
    timer = 6
    sense.clear()
    sense.stick.direction_any = pushed
    while (cancelled == False and timer > 0):
        numled.show_number(sense, 0, colors[0])
        time.sleep(.25)
        numled.show_number(sense, 0, colors[1])
        time.sleep(.25)
        sense.clear()
        timer -= 1
    cancelled = False
    return was_cancelled
