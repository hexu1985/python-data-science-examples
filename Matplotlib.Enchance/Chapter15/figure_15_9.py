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
y = [math.log(value,math.e) for value in x]

plt.plot(x,y,ls="-",lw=2,color="r")

plt.text(4.0,2.1,r"$\mathrm{\begin{pmatrix} \ln{e^{2}}&2 \\ 1&\ln{e} \end{pmatrix}}$",fontsize=20)
plt.text(12.0,2.3,r"$\mathrm{y=\ln{x}}$",fontsize=20)
#(e,1)
plt.axhline(y=1,ls=":",lw=1,color="c")
plt.axvline(x=math.e,ls=":",lw=1,color="c")
#(e^2,2)
plt.axhline(y=2,ls=":",lw=1,color="c")
plt.axvline(x=(math.e)*(math.e),ls=":",lw=1,color="c")

plt.show()
