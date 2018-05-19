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

def pushed(event):
    if event.action != ACTION_RELEASED:
        numled.show_number(sense, 10, colors[0])
        time.sleep(.5)
        numled.show_number(sense, 10, colors[1])
        time.sleep(.5)
        sense.clear()
        
def warn():
    sense.clear()
    for i in range(0, 5):
        sense.stick.direction_any = pushed
        numled.show_number(sense, 0, colors[i % len(colors)])
        time.sleep(.2)
        
        
warn()
