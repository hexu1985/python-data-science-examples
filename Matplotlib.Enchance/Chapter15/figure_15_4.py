import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt

from matplotlib import rc,rcParams

rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]
rcParams["text.usetex"]=True
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"],"size":16})


# set sample data
x = np.linspace(0,10,10000)
y = np.sin(x)*np.cos(x)

plt.plot(x,y,ls="-",lw=2,color="c",alpha=0.3)

plt.text(1,0.02,r"$\mathrm{\bar x = \frac{\sum_{i=1}^n x_i}{n}}$",fontsize=20)
plt.axhline(y=0,ls=":",lw=2,color="r")

plt.show()
