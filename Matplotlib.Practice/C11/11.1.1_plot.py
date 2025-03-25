import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.axes([0.1,0.1,.8,.8], frameon=True,facecolor='y',aspect="equal")
plt.plot(2+np.arange(3), [0,1,0])
plt.title("Line Chart")

# Add text in string 'Text instance' to axis at location 'x', 'y', data
# coordinates
plt.text(2.25, .8, "FONT")

plt.show()

