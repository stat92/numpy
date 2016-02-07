import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

x = np.arange(5)
y = np.random.randn(5)

fig, axes = plt.subplots(ncols=2,figsize=plt.figaspect(1./2))

vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
horiz_bars = axes[1].barh(x, y, color='lightblue', align='center')

for bar in vert_bars:
	if bar.xy[1] < 0:
		bar.set(edgecolor='darkred', color='salmon', linewidth=3)

for x,y in zip(x,y):
	axes[0].text(x+0.05, y+0.05, '%.1f' % y, ha='center', va='bottom')

axes[0].axhline(0, color='gray', linewidth=2)
axes[1].axvline(0, color='gray', linewidth=2)

plt.show()
