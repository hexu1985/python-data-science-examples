import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import math

from matplotlib import rc,rcParams

rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]
rcParams["text.usetex"]=True
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"],"size":16})

# set sample data
x = np.linspace(0,10,10000)
y = x*np.power(math.e,(-x**2))

plt.plot(x,y,ls="-",lw=2,color="r")

plt.text(1,0.39,r"$\mathrm{\max_{0\leq{x}\leq10} xe^{-{x}^2}}$",fontsize=20)
plt.axhline(y=np.max(x*np.power(math.e,(-x**2))),ls=":",lw=2,color="c")

plt.show()
