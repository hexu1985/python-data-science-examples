import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# usage of package matplotlib
mpl.rcParams["lines.linewidth"]=2
mpl.rcParams["lines.color"]="c"
mpl.rcParams["lines.linestyle"]="--"

# normal plot
plt.axes([0.1,0.7,.3,.3], frameon=True,facecolor='y',aspect="equal")
plt.plot(np.arange(3), [0,1,0])
plt.cla()
plt.plot(np.arange(3), [0,1,0])

# no-plt
plt.axes([0.4,0.4,.3,.3], frameon=True,facecolor='y',aspect="equal")
plt.plot(2+np.arange(3), [0,1,0])

# no-axes
plt.axes([0.7,0.1,.3,.3], frameon=True,facecolor='y',aspect="equal")
plt.plot(4+np.arange(3), [0,1,0])
plt.axis("off")

plt.show()

