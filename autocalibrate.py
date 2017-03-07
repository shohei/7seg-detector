#!/usr/bin/env python
#-*- coding:utf-8 -*-

import serial
import threading
import sys
import time
import commands
import os

try:
    status, output = commands.getstatusoutput("ls /dev/tty.usb*")
    dev_port = output
    s = serial.Serial(port=dev_port,baudrate=115200)
except Exception:
    print "No usb device found."
    exit()

s.setDTR(True);
time.sleep(1);
s.setDTR(False)

fout = open("result.txt",'w')

rod1 = 0
rod2 = 0
rod3 = 0
X = 175
Y = 0

def parseG111Command(comm):
    return


def parseWaitCommand(comm):
    if comm.find('WAIT,') > -1:
        waittime = float(comm.split("WAIT,")[1])
        time.sleep(waittime)
        Z = detectNumber()
        fout.write(rod1,rod2,rod3,X,Y,Z) 

def detectNumber():
    # command = "fswebcam --no-timestamp --no-banner -r 1280x1024 image.jpg;\
    #         python trimmer.py; python binarize.py; \
    #         ./ssocr -d -1 bwimage.jpg z_height"
    command = "python trimmer.py; python binarize.py; \
             ./ssocr -d -1 bwimage.jpg z_height"
    os.system(command)
    _, z_height = commands.getstatusoutput("cat z_height.txt")
    z_height = float(z_height)
    return z_height

def thread2():
    line = ""
    while True:
        data = s.read()
        if data=="\n":
            print line
            parseWaitCommand(line)
            line = ""
            continue
        line += data

t2 = threading.Thread(target=thread2)
t2.start()

print "Press <Enter> to exit."
print "Wait a moment for initializing......"
while(True):
    try:
        key = raw_input()
        if key.find('G111') > -1:
            parseG111Command(key)
        if(key==""):
            t2._Thread__stop()
            exit()
        key += "\n"
        s.write(key)
    except Exception:
        #print "\nstop thread2"
        t2._Thread__stop()
        exit()

fout.close()
