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

def cancel(sck, host, port):
    print("CANCEL")
    try :
        # set the whole string
        sck.sendto("CANCEL", (host, port))
        # receive data from client (data, addr)
        d = sck.recvfrom(1024)
        reply = d[0]
        addr = d[1]
        
        print ('Server reply : ' + reply)
     
    except (socket.error, msg):
        print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    
def sos():
    print("SOS")
    
def send(sck, host, port):
    global cancelled
    cancelled = False
    sos()
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
        cancel(sck, host, port)
    
    