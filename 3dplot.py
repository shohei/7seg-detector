import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

coord = [(175,0,-1.5),
(123,123,-0.5),
(0,175,0.6),
(-123,123,0.6),
(-175,0,-0.6),
(-123,-123,-1.4),
(0,-175,1),
(123,-123,0.8)]

xs = []
ys = []
zs = []
        
for c in coord:
    x = c[0]
    y = c[1]
    z = c[2]
    xs.append(x)
    ys.append(y)
    zs.append(z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

