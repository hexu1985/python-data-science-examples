# -*- coding: utf-8 -*-
"""
Listing 1-1. PLOTTING_AREA
"""

import numpy as np
import matplotlib.pyplot as plt

x1=-10
x2=10
y1=-10
y2=10
plt.xlim(x1, x2)
plt.ylim(y1, y2)

plt.axis('on')
plt.grid(True)

plt.show()

