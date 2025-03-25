import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi,2*np.pi,200)
y = np.sin(x)
y1 = np.cos(x)

# set figure #1
plt.subplot(121)

plt.plot(x,y)

# set figure #2
plt.subplot(122)

plt.plot(x,y1)

plt.show()
