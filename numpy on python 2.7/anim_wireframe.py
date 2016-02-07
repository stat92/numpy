from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

base = [0,0.2,0.3,0.6,0.9,0.8,0.6,0.3,0.2,0.1]

def _update(i):
    ax.clear()
    ax.set(xlim=[0,50],ylim=[1,4],zlim=[-2,2],xlabel='x',ylabel='y',zlabel='z')
    x = np.arange(0,i,0.1)
    p = base[i%10]
    y = np.arange(1.5+p,3.5-p,0.1)
    x, y = np.meshgrid(x,y)
    z = np.sin(x)
    ax.plot_wireframe(x, y, z, rstride=1, cstride=1)
    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

anim = animation.FuncAnimation(fig, _update, frames=40, interval=100, repeat=False)

plt.show()