import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,1000)
y = 0.9*np.sin(np.pi*x)

fig,ax = plt.subplots(2,3)

# subplot(2,3,1)
ax[0,0].plot(x,y,lw=3,color="steelblue")

ax[0,0].spines["right"].set_visible(False)
ax[0,0].spines["top"].set_visible(False)

# set left and bottom spines position
ax[0,0].spines["left"].set_position(("data",0.5))
ax[0,0].spines["bottom"].set_position(("data",1))

# set tickline position of bottom and left spines
ax[0,0].xaxis.set_ticks_position("bottom")
ax[0,0].yaxis.set_ticks_position("left")

ax[0,0].set_ylim(-1,1)
ax[0,0].set_facecolor("lemonchiffon")

# subplot(2,3,4)
ax[1,0].plot(x,y,lw=3,color="steelblue")

ax[1,0].spines["right"].set_color("none")
ax[1,0].spines["top"].set_color("none")

# set left and bottom spines position
ax[1,0].spines["left"].set_position("zero")
ax[1,0].spines["bottom"].set_position("zero")

# set tickline position of bottom and left spines
ax[1,0].xaxis.tick_bottom()
ax[1,0].yaxis.tick_left()

ax[1,0].set_ylim(-1,1)
ax[1,0].set_facecolor("lemonchiffon")

# subplot(2,3,2)
ax[0,1].plot(x,y,lw=3,color="steelblue")

ax[0,1].spines["right"].set_visible(False)
ax[0,1].spines["top"].set_visible(False)

# set left and bottom spines position
ax[0,1].spines["left"].set_position(("axes",0.25))
ax[0,1].spines["bottom"].set_position(("axes",0.75))

# set tickline position of bottom and left spines
ax[0,1].xaxis.set_ticks_position("bottom")
ax[0,1].yaxis.set_ticks_position("left")

ax[0,1].set_ylim(-1,1)
ax[0,1].set_facecolor("lemonchiffon")

# subplot(2,3,5)
ax[1,1].plot(x,y,lw=3,color="steelblue")

ax[1,1].spines["right"].set_color("none")
ax[1,1].spines["top"].set_color("none")

# set left and bottom spines position
ax[1,1].spines["left"].set_position("center")
ax[1,1].spines["bottom"].set_position("center")

# set tickline position of bottom and left spines
ax[1,1].xaxis.tick_bottom()
ax[1,1].yaxis.tick_left()

ax[1,1].set_ylim(-1,1)
ax[1,1].set_facecolor("lemonchiffon")

# subplot(2,3,3)
ax[0,2].plot(x,y,lw=3,color="steelblue")

ax[0,2].spines["right"].set_visible(False)
ax[0,2].spines["top"].set_visible(False)

# set left and bottom spines position
ax[0,2].spines["left"].set_position(("outward",3))
ax[0,2].spines["bottom"].set_position(("outward",2))

# set tickline position of bottom and left spines
ax[0,2].xaxis.set_ticks_position("bottom")
ax[0,2].yaxis.set_ticks_position("left")

ax[0,2].set_ylim(-1,1)
ax[0,2].set_facecolor("lemonchiffon")

# subplot(2,3,6)
ax[1,2].plot(x,y,lw=3,color="steelblue")

ax[1,2].spines["right"].set_color("none")
ax[1,2].spines["top"].set_color("none")

# set left and bottom spines position
ax[1,2].spines["left"].set_position(("outward",-3))
ax[1,2].spines["bottom"].set_position(("outward",-2))

# set tickline position of bottom and left spines
ax[1,2].xaxis.tick_bottom()
ax[1,2].yaxis.tick_left()

ax[1,2].set_ylim(-1,1)
ax[1,2].set_facecolor("lemonchiffon")

fig.subplots_adjust(wspace=0.35,hspace=0.2)

plt.show()
