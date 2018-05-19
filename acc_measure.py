#!/usr/bin/python3
import time
import datetime
import math
import numled

from sense_hat import SenseHat
sense = SenseHat()

colors = [(255, 0, 0), (255, 255, 255)]

def get_acceleration(a, b):
    x1 = a['x']
    x2 = b['x']
    
    y1 = a['y']
    y2 = b['y']
    
    z1 = a['z']
    z2 = b['z']
    
    xsum = (x1 - x2)**2
    ysum = (y1 - y2)**2
    zsum = (z1 - z2)**2
    
    acceleration = math.sqrt(xsum + ysum + zsum)
    return acceleration


def warn():
    for i in range(0, 5):
        numled.show_number(sense, 0, colors[i % len(colors)])
        time.sleep(.2)
    
# Logging function with the temperature value as argument
def log_acceleration_to_file():
    # Open (or create if not exists) the file named "acceleration.txt"
    # in "append" mode
    temp_log = open("acceleration.txt", "a")
    
    # Write the line to the given file
    measure1 = sense.get_accelerometer_raw()
    time.sleep(.25)
    measure2 = sense.get_accelerometer_raw()
    
    acceleration = get_acceleration(measure1, measure2)
    
    lcltm = str(datetime.datetime.now())
    temp_log.write("[" + lcltm + "]  A: %.2f \n" % acceleration)
    
    # Close the file after writing
    temp_log.close()
    
    if (acceleration > 1):
        warn()
    time.sleep(.25)
    
sense.clear()
temp_log = open("acceleration.txt", "w")
#print("Acceleration:", acceleration)
while True:
    log_acceleration_to_file()
