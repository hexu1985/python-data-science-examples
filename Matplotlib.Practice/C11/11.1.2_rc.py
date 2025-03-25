import matplotlib.pyplot as plt
import numpy as np

# line properties in change
plt.rcParams["lines.linewidth"] = 8.0
plt.rcParams["lines.linestyle"] = "--"

# font properties in change
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "New Century Schoolbook"
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.variant"] = "small-caps"
plt.rcParams["font.weight"] = "black"
plt.rcParams["font.size"] = 12.0

# text properties in change
plt.rcParams["text.color"] = "blue"

plt.axes([0.1,0.1,.8,.8], frameon=True,facecolor='y',aspect="equal")
plt.plot(2+np.arange(3), [0,1,0])
plt.title("Line Chart")

# Add text in string 'Text instance' to axis at location 'x', 'y', data
# coordinates
plt.text(2.25, .8, "FONT")

plt.show()

