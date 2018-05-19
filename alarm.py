#!/usr/bin/python3
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

import time
import datetime
import math
import numled

from sense_hat import SenseHat
sense = SenseHat()

cancelled = False
colors = [(255, 0, 0), (255, 255, 255)]

def pushed(event):
    global cancelled
    if event.action != ACTION_RELEASED:
        cancelled = True
        time.sleep(1)
        numled.show_number(sense, 10, colors[0])
        time.sleep(.5)
        numled.show_number(sense, 10, colors[1])
        time.sleep(.5)
        sense.clear()

def cancel():
    print("CANCEL")
    
def send():
    global cancelled
    sense.stick.direction_any = pushed
    while (cancelled == False):                
        numled.show_number(sense, 11, colors[0])
        time.sleep(.2)
        numled.show_number(sense, 12, colors[1])
        time.sleep(.2)
        numled.show_number(sense, 11, colors[0])
        time.sleep(.2)
        sense.clear()
        time.sleep(.2)
    if (cancelled):
        cancel()
    cancelled = False
    