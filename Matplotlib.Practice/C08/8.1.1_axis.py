import matplotlib.pyplot as plt
import numpy as np

# set #1 plot
plt.axes([0.05,0.7,.3,.3], frameon=True,facecolor='y',aspect="equal")
plt.plot(np.arange(3), [0,1,0], color="blue", linewidth=2, linestyle="--")

# set #2 plot
plt.axes([0.3,0.4,.3,.3], frameon=True,facecolor='y',aspect="equal")
plt.plot(2+np.arange(3), [0,1,0], color="blue", linewidth=2, linestyle="-")

# set #3 plot
plt.axes([0.55,0.1,.3,.3], frameon=True,facecolor='y',aspect="equal")
plt.plot(4+np.arange(3), [0,1,0], color="blue", linewidth=2, linestyle=":")

plt.show()

