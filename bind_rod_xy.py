fin1 = open("rod.csv",'r').readlines()
fin2 = open("xy.csv",'r').readlines()

fout = open("config.txt",'w')

for rod in fin1:
    rod = rod.rstrip()
    for xy in fin2:
        xy = xy.rstrip()
        print rod+','+xy
        fout.write(rod+','+xy+"\n")

fout.close()
