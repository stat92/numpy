import numpy as np
import matplotlib.pyplot as plt

names = ['Signal 1','Signal 2','Signal 3']
x = np.linspace(0,10,100)

xp = 2*np.pi # coordinate x of point

def get_y(x):
	return np.cos(x)

fig, axes = plt.subplots(nrows=3,sharex=True)


for i, ax, name in zip(range(3), axes, names):
	ax.plot(x,get_y(x+i))
	ax.set_title(name)
	ax.set(ylim=[-1.5, 1.5])
	ax.spines['bottom'].set_position('zero')	
	ax.plot( [0, xp],  [get_y(xp+i),get_y(xp+i)],  'r--',
		     [xp,xp],  [0,get_y(xp+i)],            'r--' )
	ax.scatter([xp,], [get_y(xp+i),], color='r')
	ax.annotate(r'Here',
            xy=(xp, get_y(xp+i)), xycoords='data',
            xytext=(+5, +20), textcoords='offset points', fontsize=11,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
          [r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+3\pi/2$', r'$2\pi$'])


plt.show()