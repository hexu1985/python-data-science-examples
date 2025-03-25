import matplotlib.pyplot as plt
import scipy.misc as msc

from os.path import basename,dirname,join

def filterMode():
    boxFilter = ["none","blur",
                 "edge_enhance","edge_enhance_more",
                 "emboss","sharpen","contour","smooth_more"]
    return boxFilter

def readImage(fname):
    image = msc.imread(fname)
    return image
    
def saveFilterImage(fname):
    boxFilter = filterMode()
    image = msc.imread(fname)
    directName = dirname(fname)
    fileName = basename(fname)
    subName = fileName.split(".")[0]
    extenName = fileName.split(".")[1]
    for i,name in enumerate(boxFilter):
        if name != "none":
            saveDirectory = join(directName,
                                 "{}_{}.{}".format(subName,
                                                   name,
                                                   extenName))
            msc.imsave(saveDirectory,msc.imfilter(image,name))

def showFilterImage(fname):
    font = dict(family="monospace",weight="black")
    image = readImage(fname)
    boxFilter = filterMode() 
    rows = 2
    cols = int(len(boxFilter)/2)
    fig,ax = plt.subplots(rows,cols)
    k = 0
    for row in range(rows):
        for col in range(cols):
            if boxFilter[k] != "none":
                ax[row,col].imshow(msc.imfilter(image,boxFilter[k]))
                ax[row,col].set_title(boxFilter[k],**font)
                ax[row,col].set_axis_off()
            else:
                ax[row,col].imshow(image)
                ax[row,col].set_title("source_image",**font)
                ax[row,col].set_axis_off()
            k+=1

    fig.subplots_adjust(left=0.03,right=0.97,
                        bottom=0.15,top=0.85,
                        hspace=0.005,wspace=0.02)

    plt.show()

    
def main(fname):
    saveFilterImage(fname)
    showFilterImage(fname)
    

if __name__ == "__main__":
    try:
        main(r"D:\filterimage\tree_image.jpg")
    except Exception as exc:
        print(exc)
