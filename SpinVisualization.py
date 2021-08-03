import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

nr = 8 # The number of Row
nc = 8 # The number of Column
plotx = 1
ploty = 1
spin = np.loadtxt('./spin111.csv', delimiter=',')

spinplot = np.zeros([plotx*ploty, nr, nc])
for i in range(plotx):
    for j in range(ploty):
        spinplot[i*plotx+j] = np.zeros([nr,nc])

for x in range(plotx*ploty):
    for i in range(nr):
        for j in range(nc):
            spinplot[x,i,j] = spin[i*nr+j, x]

# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue'])
bounds = [-2, 0, 2]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots(plotx, ploty, tight_layout=True)
for i in range(plotx):
    for j in range(ploty):
        ax[i,j].set_title(f"{i*ploty+j}", fontsize=12)
        ax[i,j].imshow(spinplot[i*ploty+j], interpolation='none', cmap=cmap, extent=[0, nr, 0, nc], norm=norm, zorder=0)
    
#draw gridlines1
for x in range(nr + 1):
    for i in range(plotx):
        for j in range(ploty):
            ax[i,j].axhline(x, lw=1, color='k', zorder=5)
            ax[i,j].axvline(x, lw=1, color='k', zorder=5)
            ax[i,j].axis('off')

plt.show()