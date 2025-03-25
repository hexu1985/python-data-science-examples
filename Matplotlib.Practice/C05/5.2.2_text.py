import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0,10,40)
y = np.random.randn(40)

plt.plot(x,y,ls="-",lw=2,
        marker="o",
        ms=20,
        mfc="orange",
        alpha=0.6)

plt.grid(ls=":",color="gray",alpha=0.5)

plt.text(6,0, "Matplotlib", size=30, rotation=30.,
        bbox=dict(boxstyle="round",
            ec="#8968CD",
            fc="#FFE1FF"))

plt.show()
