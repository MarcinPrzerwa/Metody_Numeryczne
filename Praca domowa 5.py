import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dt = 0.001
N = 200000
x0, y0, z0 = 1, 1, 25
list = [[], [], []]

def RownL(xyz, s=10, r=28, b=8 / 3):
    return [-s * xyz[0] + s * xyz[1], -xyz[0] * xyz[2] + r * xyz[0] - xyz[1], xyz[0] * xyz[1] - b * xyz[2]]

def algorytm():
    xyz = [x0, y0, z0]
    for n in range(N):
        K0 = RownL(xyz)
        K1 = RownL([x + k * 0.5 * dt for x, k in zip(xyz, K0)])
        K2 = RownL([x + k * 0.5 * dt for x, k in zip(xyz, K1)])
        K3 = RownL([x + k * dt for x, k in zip(xyz, K2)])
        for i in range(3):
            xyz[i] += (K0[i] + 2 * K1[i] + 2 * K2[i] + K3[i]) * dt / 6
            list[i].append(xyz[i])
    return [list[0], list[1], list[2]]

fig = plt.figure(figsize=(10, 10))
ax = Axes3D(fig)
ax.plot(algorytm()[0], algorytm()[1], algorytm()[2], linewidth=0.1)
plt.show()