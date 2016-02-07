from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def _update(i):
    ax.clear()
    ax.set(xlim=[0,10],ylim=[0,10],zlim=[0,10],xlabel='x',ylabel='y',zlabel='z')
    x = np.random.rand(15)*10
    y = np.random.rand(15)*10  
    z = np.random.rand(15)*10

    ax.scatter(x, y, z)
    

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

anim = animation.FuncAnimation(fig, _update, frames=10, interval=10)

#anim.save('sin.mp4', writer='mencoder')

plt.show()

