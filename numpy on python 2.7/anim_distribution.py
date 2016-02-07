import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.mlab as mlab


class NormalDistribution(object):

	def __init__(self):

		self.fig = plt.figure(figsize=(6,6))
		self.ax = self.fig.add_subplot(111)
		self.fig.suptitle('Normal distribution probability density function plots',fontsize=14)
		self.x = np.linspace(-7,7,200)
		self.data = [{'mu': 0, 'sigma_squared': 0.6},
		        	 {'mu': 0, 'sigma_squared': 3},
		        	 {'mu': -1, 'sigma_squared': 2},
		        	 {'mu': 0, 'sigma_squared': 1},
		         	 {'mu': 1, 'sigma_squared': 3}]			
		self.anim = animation.FuncAnimation(self.fig, self._update_plot, 
			             frames=5, interval=1000)


	def _update_plot(self, i):
		
		mu = self.data[i]['mu']
		ss = self.data[i]['sigma_squared']

		self.ax.clear()
		self.ax.plot(self.x,mlab.normpdf(self.x, mu, np.sqrt(ss)),'k')
		
		self.ax.grid(axis='both',color='y',linestyle='--',linewidth=1)
		self.ax.legend([(r'$\mu=%s, \sigma^2= %s$' % (mu, ss))], fontsize=12)
		self.ax.set(xlim=[-5,5], ylim=[0,0.6])
		self.ax.set_xlabel('X')
		self.ax.set_ylabel('Function')
		
		return self.ax


	def show(self):
		try:
			plt.show()
		except AttributeError as e:
            # eat error from lib
			pass
            #print "Exception {0}".format(e)


	def save(self):
		self.anim.save(filename='dist_normal.mp4', writer='mencoder')


def main():
    c = NormalDistribution()
    c.show()
    #c.save()

if __name__ == '__main__':
    main()