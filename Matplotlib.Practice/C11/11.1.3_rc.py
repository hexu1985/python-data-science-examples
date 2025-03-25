import matplotlib.pyplot as plt
import numpy as np

plt.axes([0.1,0.1,.8,.8], frameon=True,facecolor='y',aspect="equal")
# line properties in change
plt.plot(2+np.arange(3), [0,1,0],linewidth=8.0,linestyle="--")
plt.title("Line Chart",color="red",family="New Century Schoolbook",
        style="normal",variant="small-caps",weight="black",size=18)

# Add text in string 'Text instance' to axis at location 'x', 'y', data
# coordinates
# font properties and text properties in change
plt.text(2.25, .8, "FONT", color="blue",
        fontdict={"family":"New Century Schoolbook","style":"normal",
            "variant":"small-caps","weight":"black","size":28})

plt.show()

