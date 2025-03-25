import matplotlib.pyplot as plt

from matplotlib.cbook import get_sample_data
from matplotlib.patches import Circle

import pathlib

current_dir = pathlib.Path(__file__).parent
print(current_dir)

with get_sample_data(current_dir/"sunflower.png",asfileobj=True) as imageFile:
    imageArray = plt.imread(imageFile)

fig,ax = plt.subplots(1,1)
ai = ax.imshow(imageArray)
patch = Circle((605,360),radius=350,transform=ax.transData)
ai.set_clip_path(patch)

ax.set_axis_off()

plt.show()
