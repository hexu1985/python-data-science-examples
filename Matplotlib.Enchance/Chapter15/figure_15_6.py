import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import math

from matplotlib import rc,rcParams

rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]
rcParams["text.usetex"]=True
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"],"size":16})

# set sample data
x = np.linspace(1,10,10000)
y = np.power(1+1/x,x)

plt.plot(x,y,ls="-",lw=2,color="c",alpha=0.3)

plt.text(1,2.64,r"$\mathrm{\lim_{n\to\infty}(1+\frac{1}{n})^{n}}$",fontsize=20)
plt.axhline(y=math.e,ls=":",lw=2,color="r")

plt.show()
