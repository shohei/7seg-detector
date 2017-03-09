#!/usr/bin/env python

fin = open("result.txt",'r').readlines()
last = (-9999,-9999,-9999)

sum = 0
for line in fin:
    rod1 = line.split(",")[0].rstrip()
    rod2 = line.split(",")[1].rstrip()
    rod3 = line.split(",")[2].rstrip()
    current = (rod1,rod2,rod3)
    X = line.split(",")[3].rstrip()
    Y = line.split(",")[4].rstrip()
    z_height = line.split(",")[5].rstrip()

    if last == current:
    	#same pair
    	sum += 	z_height
    else:
    	#new pair
    	sum = z_height 


print "ranking: "



