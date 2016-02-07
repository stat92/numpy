import numpy as np 
import matplotlib.pyplot as plt 

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.fill_between(X, Y + 1, 1, color='yellow', alpha=1.00)

plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.fill_between(X, Y - 1, -1, (Y - 1) > -1, color='yellow', alpha=1.00)
plt.fill_between(X, Y - 1, -1, (Y - 1) < -1, color='red', alpha=1.00)

plt.show()