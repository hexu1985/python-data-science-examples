import matplotlib.pyplot as plt
import numpy as np

from basic_units import cm,inch

x = np.linspace(0,10,6)
cm_x = [i*cm for i in x]

fig,ax = plt.subplots(2,2)

ax[0,0].plot(cm_x,cm_x,ls="-",lw=3,color="k",xunits=cm,yunits=cm)
ax[0,0].set_ylabel("")
ax[0,0].set_xlabel("")

ax[0,1].plot(cm_x,cm_x,ls="--",lw=3,color="cornflowerblue",xunits=cm,yunits=inch)
ax[0,1].set_ylabel("")
ax[0,1].set_xlabel("")
ax[0,1].set_xlim(2,8)

ax[1,0].plot(cm_x,cm_x,ls="-.",lw=3,color="gold",xunits=inch,yunits=cm)
ax[1,0].set_ylabel("")
ax[1,0].set_xlabel("")
ax[1,0].set_xlim(2*cm,8*cm)

ax[1,1].plot(cm_x,cm_x,ls=":",lw=3,color="purple",xunits=inch,yunits=inch)
ax[1,1].set_ylabel("")
ax[1,1].set_xlabel("")

plt.show()
