# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,2,1000)
y = np.exp(x)

plt.plot(x,y,ls="-",lw=2,color="g")

plt.title("center demo")
plt.title("Left Demo",loc="left",
        fontdict={"size":"xx-large",
            "color":"r",
            "family":"Times New Roman"})
plt.title("right demo", loc="right",
        family="Comic Sans MS",
        size=20,
        style="oblique",
        color="c")

plt.show()
