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

unitsA = [-3,-4,-5] 
unitsC = [3,4,5] 
rod_offsets = list(itertools.product(unitsA, unitsC)) # Tower A,B,C

fout = open("config.txt",'w')

for rod_offset in rod_offsets:
    for c in coordinates:
        mylist = rod_offset+c
        print "{0[0]},0,{0[1]},{0[2]},{0[3]}\n".format(mylist)
        fout.write("{0[0]},0,{0[1]},{0[2]},{0[3]}\n".format(mylist)
)

fout.close()


