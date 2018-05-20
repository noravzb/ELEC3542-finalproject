#!/usr/bin/python3
import time
import datetime
import math
import numled
import joystick
import alarm
import socket   #for sockets
import sys  #for exit
import acc_measure

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

# Logging function with the temperature value as argument
def log_acceleration(sck, host, port):
    # Open (or create if not exists) the file named "acceleration.txt"
    # in "append" mode
    temp_log = open("acceleration.txt", "a")
    
    # Write the line to the given file
    measure1 = sense.get_accelerometer_raw()
    time.sleep(.25)
    measure2 = sense.get_accelerometer_raw()
    
    acceleration = get_acceleration(measure1, measure2)
    acceleration = round(acceleration, 2)
    
    lcltm = str(datetime.datetime.now())
    temp_log.write("[" + lcltm + "]  A: %.2f \n" % acceleration)
    
    # Close the file after writing
    temp_log.close()
    
    if (acceleration > 1):
        print("[" + lcltm + "]  A: %.2f \n" % acceleration)
        cancelled = joystick.warn()
        
        if (cancelled == False):
            try :
                # set the whole string
                sck.sendto("ALARM", (host, port))
                # receive data from client (data, addr)
                d = sck.recvfrom(1024)
                reply = d[0]
                addr = d[1]
        
                print ('Server reply : ' + reply)
     
            except (socket.error, msg):
                print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
                sys.exit()
        
            alarm.send(sck, host, port)
        
    time.sleep(.25)
    return (lcltm, acceleration)

sense.clear()
temp_log = open("acceleration.txt", "w")
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print ('Failed to create socket')
    sys.exit()
 
host = raw_input("Specify host to connect to: ")

port = 8888;
 
while(1) :
    msg = log_acceleration(s, host, port)
    
    try :
        #Set the whole string
        s.sendto(str(msg[1]), (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
        
        print ('Server reply : ' + reply)
     
    except (socket.error, msg):
        print ('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
