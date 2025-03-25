import matplotlib.pyplot as plt
import numpy as np

from basic_units import secs,minutes,hertz

t = [2,4,3,5,8,6,7,9]
secs_t = [time*secs for time in t]

fig,ax = plt.subplots(3,1,sharex=True)

ax[0].scatter(secs_t,secs_t,s=10*np.max(t),c="steelblue",marker="o")
ax[0].set_xlabel("")
ax[0].set_ylabel("")

ax[1].scatter(secs_t,secs_t,s=10*np.max(t),c="gold",marker="D",yunits=hertz)
ax[1].set_xlabel("")
ax[1].set_ylabel("")
ax[1].axis([1,10,0,1])

ax[2].scatter(secs_t,secs_t,s=10*np.max(t),c="brown",marker="^",yunits=hertz)
ax[2].yaxis.set_units(minutes)
ax[2].set_xlabel("")
ax[2].set_ylabel("")
ax[2].axis([1,10,0,1])

fig.subplots_adjust(hspace=0.2)

plt.show()
