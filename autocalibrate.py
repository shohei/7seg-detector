#!/usr/bin/env python
#-*- coding:utf-8 -*-

import serial
import threading
import sys
import time
import commands
import os
import traceback

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def eprint(words):
    print bcolors.FAIL + words + bcolors.ENDC

def pprint(words):
    print bcolors.WARNING + words + bcolors.ENDC

def okprint(words):
    print bcolors.OKGREEN + words + bcolors.ENDC

def ackprint(words):
    print bcolors.OKBLUE + words + bcolors.ENDC

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
radiusA = 0
radiusB = 0
radiusC = 0
X = 0 
Y = 0


class Pref():
    def __init__(self):
	self.machineBusy = False
        self.success = 0
        self.fail = 0
#class Pref():
#    def __init__(self):
#        self.rod1 = 0
#        self.rod2 = 0
#        self.rod3 = 0
#        self.X = 0 
#        self.Y = 0

def setRodTrim(a,b,c):
    comm = "M665 A"+a+" B"+b+" C"+c
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def setRadiusTrim(o,p,q):
    comm = "M665 O"+o+" P"+p+" Q"+q
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def goToPlaneCenter():
    comm = "G1 X0 Y0"
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def setOrigin():
    comm = "G28"
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def goToInitialPosition():
    comm = "G1 Z300 F4000"
    print comm
    for c in comm:
        s.write(c)
    s.write("\r")

def startCalibration():
    print "setOrigin()"
    setOrigin()
    pref.machineBusy=True
    lockUntilOk()

    print "goToInitialPosition()"
    goToInitialPosition()
    pref.machineBusy=True
    lockUntilOk()

    print "parseCalibrateConfig()"
    parseCalibrateConfig()

def parseCalibrateConfig():
    fin = open("config.txt",'r').readlines()
    lineNumber = 1
    for line in fin:
        rod1 = line.split(",")[0].rstrip()
        rod2 = line.split(",")[1].rstrip()
        rod3 = line.split(",")[2].rstrip()
        radius1 = line.split(",")[3].rstrip()
        radius2 = line.split(",")[4].rstrip()
        radius3 = line.split(",")[5].rstrip()
        X = line.split(",")[6].rstrip()
        Y = line.split(",")[7].rstrip()

        print "setRodTrim()"
        setRodTrim(rod1,rod2,rod3)
        pref.machineBusy=True
        lockUntilOk()

        pprint("setRadiusTrim()")
        setRadiusTrim(radius1,radius2,radius3)
        pref.machineBusy=True
        lockUntilOk()

        sendLineMove(X,Y)

	pref.machineBusy=True
        lockUntilOk()

        z_height = detectNumber()
        try:
            z_height = float(z_height)
            #okprint("{0},{1},{2},{3},{4},{5}\n".format(rod1,rod2,rod3,X,Y,z_height)) 
            #fout.write("{0},{1},{2},{3},{4},{5}\n".format(rod1,rod2,rod3,X,Y,z_height))
            okprint("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(rod1,rod2,rod3,radius1,radius2,radius3,X,Y,z_height)) 
            fout.write("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(rod1,rod2,rod3,radius1,radius2,radius3,X,Y,z_height))
            pprint("processed config line "+str(lineNumber))
            lineNumber += 1
            pref.success += 1
        except:
          eprint(traceback.format_exc())
          pref.fail += 1
          continue

    pprint("calibration done.") 
    eprint("Success rate: "+str(pref.success/((pref.success+pref.fail)*1.0)))
    goToPlaneCenter()
    os.system("cp -p result.txt result_`date '+%Y%m%d_%H%M%S'`.txt")

# def parseWaitCommand(comm):
#     if comm.find('WAIT,') > -1:
#         waittime = float(comm.split("WAIT,")[1])
#         time.sleep(waittime)
#         Z = detectNumber()
#         fout.write(str(rod1)+","+str(rod2)+","+str(rod3)+","+str(X)+","+str(Y)+","+str(Z)) 

def checkMachineState(comm):
     if comm.find('ok') > -1:
	ackprint("ACK RECEIVED")
	pref.machineBusy=False

def sendLineMove(_X,_Y):
    comm = "G1 X"+_X+" Y"+_Y+" F4000"
    pprint(comm) 
    for c in comm:
        s.write(c)
    s.write("\r")

def lockUntilOk():
    while pref.machineBusy==True:
        time.sleep(1)

def detectNumber():
    command = "fswebcam --no-timestamp --no-banner -r 1280x1024 image.jpg;\
            python trimmer.py; python binarize.py; \
./ssocr -d -1 bwimage.jpg | cat | perl -pe 's/_/-/g' | perl -ne 'if ($_=~/\./) {print $_} else {print substr($_,0,length($_)-2);print \".\";print substr($_,-2);}'  > z_height.txt"
    #command = "python trimmer.py; python binarize.py; \
    #         ./ssocr -d -1 bwimage.jpg > z_height.txt"
    os.system(command)
    _, z_height = commands.getstatusoutput("cat z_height.txt")
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


pprint("Press <Enter> to exit.") 
pprint("Wait a moment for initializing......")

pref = Pref()

while(True):
    try:
        key = raw_input()
        if (key=='a'):
            print bcolors.WARNING + "calibration start" + bcolors.ENDC
            startCalibration()
            continue
        if(key==""):
            t2._Thread__stop()
            exit()
        key += "\n"
        s.write(key)
    except KeyboardInterrupt:
	s.close()
        t2._Thread__stop()
	fout.close()
        exit()
    except:
        print traceback.format_exc()
	s.close()
        t2._Thread__stop()
        exit()

#fout.close()
