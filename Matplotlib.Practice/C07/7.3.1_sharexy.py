import matplotlib.pyplot as plt
import numpy as np

# create sample data:

x1 = np.linspace(0, 2*np.pi, 400)
y1 = np.cos(x1**2)

x2 = np.linspace(0.01,10,100)
y2 = np.sin(x2)

x3 = np.random.rand(100)
y3 = np.linspace(0,3,100)

x4 = np.arange(0,6,0.5)
y4 = np.power(x4,3)

# set (2,2) subplots

fig,ax = plt.subplots(2, 2)

# set chart of each subplot

ax1 = plt.subplot(221)
ax1.plot(x1,y1)

ax2 = plt.subplot(222)
ax2.plot(x2,y2)

ax3 = plt.subplot(223)
ax3.scatter(x3,y3)

ax4 = plt.subplot(224,sharex=ax1)
ax4.scatter(x4,y4)

# Show figure and subplot(s)

plt.show()
