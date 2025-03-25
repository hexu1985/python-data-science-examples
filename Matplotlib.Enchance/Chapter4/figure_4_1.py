import matplotlib.patches as patches
import matplotlib.pyplot as plt

fig = plt.figure(1, figsize=(8,9), dpi=72)
fontsize = 0.5*fig.dpi

# subplot(111)
ax = fig.add_subplot(1,1,1,frameon=False,xticks=[],yticks=[])

boxStyles = patches.BoxStyle.get_styles()
boxStyleNames = list(boxStyles.keys())
boxStyleNames.sort()

for i,name in enumerate(boxStyleNames):
    ax.text(float(i+0.5)/len(boxStyleNames),
            (float(len(boxStyleNames))-0.5-i)/len(boxStyleNames),
            name,
            ha="center",
            size=fontsize,
            transform=ax.transAxes,
            bbox=dict(boxstyle=name,fc="w",ec="k"))

plt.show()
