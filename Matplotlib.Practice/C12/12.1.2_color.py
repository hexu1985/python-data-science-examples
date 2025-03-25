import matplotlib.pyplot as plt
import numpy as np

# ColorBrewer Diverging: RdYlBu
hexHtml = ["#d73027","#f46d43","#fdae61",
            "#fee090","#ffffbf","#e0f3f8",
            "#abd9e9","#74add1","#4575b4"]

sample = 10000
fig,ax = plt.subplots(1,1)

for j in range(len(hexHtml)):
    y = np.random.normal(0,0.1,size=sample).cumsum()
    x = np.arange(sample)
    ax.scatter(x,y,
            label=str(j),
            linewidths=0.2,
            edgecolors="grey",
            facecolor=hexHtml[j])

ax.legend()

plt.show()
