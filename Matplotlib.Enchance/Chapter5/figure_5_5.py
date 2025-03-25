import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,10,1000)
y1 = [2**j for j in x]
y2 = [0.09*j for j in x]


fig,ax = plt.subplots(2,2)

# linear
ax[0,0].plot(x,y1)
ax[0,0].set_yscale("linear")
ax[0,0].set_title("linear")
ax[0,0].grid(True,ls="-",lw=1,color="gray")

# log
ax[0,1].plot(x,y1)
ax[0,1].set_yscale("log")
ax[0,1].set_title("log")
ax[0,1].grid(True,ls="-",lw=1,color="gray")

# logit
ax[1,0].plot(x,y2)
ax[1,0].set_yscale("logit")
ax[1,0].set_title("logit")
ax[1,0].grid(True,ls="-",lw=1,color="gray")
ax[1,0].set_ylim(0.1,0.9)

# symlog
ax[1,1].plot(x,y2-np.average(y2))
ax[1,1].set_yscale("symlog",linthreshy=0.02)
ax[1,1].set_title("symlog")
ax[1,1].grid(True,ls="-",lw=1,color="gray")

fig.subplots_adjust(hspace=0.3,wspace=0.3)

plt.show()
