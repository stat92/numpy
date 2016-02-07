import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0,5,100)

fig = plt.figure(figsize=(12,6))
plt.suptitle('Exponential distribution plots',fontsize=14)

##########################################################

# Exponential distribution probability density function
def get_density_y(x, RATE):	
	return RATE*np.exp(-RATE*x)


ax1 = fig.add_subplot(121,ylim=[0,1.5])
# Get exponential distribution plot
ax1.plot(x,get_density_y(x, 0.5),'r')
ax1.plot(x,get_density_y(x, 1.5),'b')
# Preferences of first plot
ax1.grid(axis='both',color='y',linestyle='--',linewidth=1)
ax1.legend([r'$\lambda=0.5$',r'$\lambda=1.5$'], fontsize=12)
ax1.set_xlabel('x')
ax1.set_ylabel(r'$P(x)$')
ax1.set_title('Probability density function', fontsize=12)

###########################################################

def get_cumulative_y(x, RATE):
	return 1-np.exp(-x*RATE)


ax2 = fig.add_subplot(122)
# Get exponential distribution plot
ax2.plot(x,get_cumulative_y(x, 0.5),'r')
ax2.plot(x,get_cumulative_y(x, 1.5),'b')
# Preferences of second plot
ax2.grid(axis='both',color='y',linestyle='--',linewidth=1)
ax2.legend([r'$\lambda=0.5$',r'$\lambda=1.5$'], fontsize=12)
ax2.set_xlabel('x')
ax2.set_ylabel(r'$P(X \leq x)$')
ax2.set_title('Cumulative distribution function', fontsize=12)

############################################################

plt.show()