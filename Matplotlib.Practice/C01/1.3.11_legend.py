import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

#plt.legend(loc="lower left")
#plt.legend(loc="upper left")
plt.legend(loc="upper right")

plt.show()
