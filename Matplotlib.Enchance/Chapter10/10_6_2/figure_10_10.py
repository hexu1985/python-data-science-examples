import matplotlib.pyplot as plt

fig,ax = plt.subplots(2,2)

font = dict(family="monospace",weight="bold")

# get the array of RGB channels 
outfile = plt.imread(r"D:\filterimage\tree_image.jpg")
print("the array 'outfile' shape: {}".format(outfile.shape))

# get the arrays of the red, green and blue channels
rCh = outfile[:,:,0]
print("the array 'rCh' shape: {}".format(rCh.shape))

gCh = outfile[:,:,1]
print("the array 'gCh' shape: {}".format(gCh.shape))

bCh = outfile[:,:,2]
print("the array 'bCh' shape: {}".format(bCh.shape))

# show source image
ax[0,0].imshow(outfile)
ax[0,0].set_title("source_image",**font)
ax[0,0].set_axis_off()

# show the images of the red, green and blue channels
ax[0,1].imshow(rCh)
ax[0,1].set_title("rCh_image",**font)
ax[0,1].set_axis_off()

ax[1,0].imshow(gCh)
ax[1,0].set_title("gCh_image",**font)
ax[1,0].set_axis_off()

ax[1,1].imshow(bCh)
ax[1,1].set_title("bCh_image",**font)
ax[1,1].set_axis_off()

plt.show()
