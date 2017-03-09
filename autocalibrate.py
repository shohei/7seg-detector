#!/usr/bin/env python
#-*- coding:utf-8 -*-

import serial
import threading
import sys
import time
import commands
import os

try:
    status, output = commands.getstatusoutput("ls /dev/ttyACM0")
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
X = 0 
Y = 0

machineBusy = False

#class Pref():
#    def __init__(self):
#        self.rod1 = 0
#        self.rod2 = 0
#        self.rod3 = 0
#        self.X = 0 
#        self.Y = 0
def setOrigin():
    comm = "G28"
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def goToInitialPosition():
    comm = "G1 Z300"
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def startCalibration():
    setOrigin()
    machineBusy=True
    lockUntilOk()

    goToInitialPosition()
    machineBusy=True
    lockUntilOk()

    parseCalibrationConfig()

def parseCalibrateConfig():
    fin = open("config.txt",'r').readlines()
    for line in fin:
        rod1 = line.split(",")[0].rstrip()
        rod2 = line.split(",")[1].rstrip()
        rod3 = line.split(",")[2].rstrip()
        X = line.split(",")[3].rstrip()
        Y = line.split(",")[4].rstrip()
        
        sendLineMove(X,Y)

	machineBusy=True
        lockUntilOk()

        Z = detectNumber()
        print str(rod1)+","+str(rod2)+","+str(rod3)+","+str(X)+","+str(Y)+","+str(Z) 
        fout.write(str(rod1)+","+str(rod2)+","+str(rod3)+","+str(X)+","+str(Y)+","+str(Z)) 

# def parseWaitCommand(comm):
#     if comm.find('WAIT,') > -1:
#         waittime = float(comm.split("WAIT,")[1])
#         time.sleep(waittime)
#         Z = detectNumber()
#         fout.write(str(rod1)+","+str(rod2)+","+str(rod3)+","+str(X)+","+str(Y)+","+str(Z)) 

def checkMachineState(comm):
     if comm.find('ok') > -1:
	machineBusy=False

def sendLineMove(_X,_Y):
    comm = "G1 X"+_X+" Y"+_Y+" F1000"
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def lockUntilOk():
    while machineBusy==True:
        time.sleep(1)

def detectNumber():
    command = "fswebcam --no-timestamp --no-banner -r 1280x1024 image.jpg;\
            python trimmer.py; python binarize.py; \
            ./ssocr -d -1 bwimage.jpg | cat | perl -ne 'print substr($_,0,length($_)-2);print \".\";print substr($_,-2);' > z_height.txt"
    #command = "python trimmer.py; python binarize.py; \
    #         ./ssocr -d -1 bwimage.jpg > z_height.txt"
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
            #parseWaitCommand(line)
            checkMachineState(line)
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
        if (key=='a'):
            print "calibration start"
            startCalibration()
        if(key==""):
            t2._Thread__stop()
            exit()
        key += "\n"
        s.write(key)
    except Exception:
        #print "\nstop thread2"
	s.close()
        t2._Thread__stop()
        exit()
    except KeyboardInterrupt:
	s.close()
        t2._Thread__stop()
	fout.close()
        exit()

#fout.close()
