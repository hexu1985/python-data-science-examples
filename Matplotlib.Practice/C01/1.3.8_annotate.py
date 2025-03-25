import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

plt.annotate("maximum",
        xy=(np.pi/2, 1.0),
        xytext=((np.pi/2)+1.0, .8),
        weight="bold",
        color="b",
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b"))

plt.show()
