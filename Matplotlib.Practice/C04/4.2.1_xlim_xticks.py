import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

# set subplot(211)
plt.subplot(211)

# plot figure
plt.plot(x,y)

# set subplot(212)
plt.subplot(212)

# set xlimit
plt.xlim(-2*np.pi, 2*np.pi)

# set ticks
plt.xticks([-2*np.pi, -3*np.pi/2, -1*np.pi, -1*(np.pi)/2, 0, 
            (np.pi)/2, np.pi, 3*np.pi/2, 2*np.pi],
        [r"$-2\pi$", r"$-3\pi/2$", r"$-\pi$", r"$-\pi/2$", r"$0$",
            r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])

# plot figure
plt.plot(x, y)
plt.show()

