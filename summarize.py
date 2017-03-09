#!/usr/bin/env python

fin = open("result.txt",'r').readlines()
for line in fin:
    rod1 = line.split(",")[0].rstrip()
    rod2 = line.split(",")[1].rstrip()
    rod3 = line.split(",")[2].rstrip()
    X = line.split(",")[3].rstrip()
    Y = line.split(",")[4].rstrip()
    z_height = line.split(",")[5].rstrip()
    print z_height








