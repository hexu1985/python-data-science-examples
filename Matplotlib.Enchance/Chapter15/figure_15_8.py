import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import math

from matplotlib import rc,rcParams

rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]
rcParams["text.usetex"]=True
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"],"size":16})

# set sample data
x = np.linspace(0.5,16,100)
y = np.array([math.log(value,2) for value in x])

plt.plot(x,y,ls="-",lw=2,color="r")

plt.text(4.0,1.6,r"$\mathrm{\log_{2}{x}}$",fontsize=20)
plt.axhline(y=1,ls=":",lw=2,color="c")
plt.axvline(x=2,ls=":",lw=2,color="c")

plt.show()
