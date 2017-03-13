import math
import itertools

x = []
y = [] 
r = 175
angles = (0,math.pi/4,math.pi/2,math.pi*3/4,math.pi,math.pi*5/4,math.pi*3/2,math.pi*7/4)

for theta in angles:
    x.append(int(round(r*math.cos(theta),1)))
    y.append(int(round(r*math.sin(theta),1)))
coordinates = zip(x,y)

trimA = [0,-3,3] 
trimB = [0,-3,3] 
trimC = [0,-3,3] 
rad_offsets = list(itertools.product(trimA, trimB, trimC)) # Tower A,B,Cl

fout = open("config.txt",'w')

for rad_offset in rad_offsets:
    for c in coordinates:
        mylist = rad_offset+c
        print "{0[0]},{0[1]},{0[2]},{0[3]},{0[4]}\n".format(mylist)
        fout.write("{0[0]},{0[1]},{0[2]},{0[3]},{0[4]}\n".format(mylist)
)

fout.close()


