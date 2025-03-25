import matplotlib.pyplot as plt
import numpy as np

from matplotlib.style.core import use

use("ggplot")

x = np.linspace(0,2*np.pi,100)
y = 1.85*np.sin(x)
y1 = 1.85*np.sin(x)+np.random.randn(100)

fig,ax = plt.subplots(2,2,sharex=True,sharey=True)

# subplot(2,2,1)
ax[0,0].scatter(x,y1,s=50,c="dodgerblue")

ax[0,0].set_ylim(-5,5)

ax[0,0].set_facecolor("lemonchiffon")

# subplot(2,2,2)
ax[0,1].plot(x,y,lw=3,color="yellowgreen")

ax[0,1].set_xlim(-1,7)
ax[0,1].set_ylim(-5,5)

ax[0,1].set_facecolor("lemonchiffon")

# subplot(2,2,3)
ax[1,0].plot(x,y,ls="--",lw=3,color="k")
ax[1,0].scatter(x,y1,s=50,c="r")

ax[1,0].set_ylim(-5,5)

ax[1,0].set_facecolor("lemonchiffon")

# subplot(2,2,4)
# non-existence

fig.suptitle("'ggplot' style of subplots(2,2)",fontsize=18,weight="bold",family="monospace")

plt.show()
