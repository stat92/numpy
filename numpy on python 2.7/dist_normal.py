import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


# Normal distribution probability density function
def get_density_y(x, ME, SIGMA):	
	# ME - mathematical expectation
	# SIGMA - variance
	part1 = 1.0/(SIGMA*np.sqrt(2.0*np.pi))
	part2 = np.exp(-0.5*pow(x-ME,2)/SIGMA**2)
	return part1*part2


fig = plt.figure(figsize=(12,6))
plt.suptitle('Normal distribution plots',fontsize=14)

ax1 = fig.add_subplot(121)

x = np.linspace(-8,8,200)

# Get normal distribution plot with function
# writed by Makha
ax1.plot(x,get_density_y(x, 0, np.sqrt(5.0)),'b')
ax1.plot(x,get_density_y(x, -2, np.sqrt(0.5)),'k')
# or with python normpdf function
#ax1.plot(x,mlab.normpdf(x, -3, np.sqrt(0.5)),'k')

ax1.grid(axis='both',color='y',linestyle='--',linewidth=1)
ax1.legend([r'$\mu=0,\sigma^2= 5.0$',r'$\mu=-2,\sigma^2= 0.5$'], fontsize=12)
ax1.set_xlabel('X')
ax1.set_ylabel('Function')
ax1.set_title('Probability density function', fontsize=12)

######################################################

# Normal distribution cumulative function
def get_cumulative_y():
	return 2




ax2 = fig.add_subplot(122)

ax2.grid(axis='both',color='y',linestyle='--',linewidth=1)
ax2.set_xlabel('X')
ax2.set_ylabel('Function')
ax2.set_title('Cumulative distribution function', fontsize=12)


plt.show()

