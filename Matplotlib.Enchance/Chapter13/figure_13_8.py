import matplotlib.pyplot as plt
import numpy as np

from matplotlib.style.core import use,available

use("fivethirtyeight")

#ColorBrewer Diverging: RdYlBu
hexHtml = ["#d73027","#f46d43","#fdae61",
                   "#fee090","#ffffbf","#e0f3f8",
                   "#abd9e9","#74add1","#4575b4"]

sample = 1000
fig,ax = plt.subplots()

for i in range(len(hexHtml)):
    y = np.random.normal(0,0.1,size=sample).cumsum()
    x = np.arange(sample)
    ax.scatter(x,y,
               label=str(i),
               linewidths=0.1,
               edgecolors="grey",
               facecolor=hexHtml[i])

ax.legend()

plt.show()
