import matplotlib.pyplot as plt
import squarify # pip install squarify

from glob import glob
from matplotlib.image import thumbnail
from os import mkdir
from os.path import basename,dirname,getsize,isdir,join
from sys import argv

if len(argv) != 3:
    print("On command line, information is not full.")
    raise SystemExit

script,indir,outdir = argv

sizeList = []
nameList = []

if not isdir(indir):
    print("Input directory %r is not found." % indir)
    raise SystemExit

if not isdir(outdir):
    print("Output directory %r is created." % outdir)
    mkdir(outdir)
else:
    print("Output directory %r has been created" % outdir)

# the image file must be PNG or Pillow-readable
for fname in glob(join(indir,"*.png")):
    indir = dirname(fname)
    filename = basename(fname)
    outfile = join(outdir,filename)
    fig = thumbnail(fname,outfile,scale=0.5)
    print("Copy %r of %r to %r" % (filename,indir,outdir))
    outfilesize = getsize(outfile)
    sizeList.append(outfilesize)
    fn = filename.split(".")
    nameList.append(fn[0])

# treemap
squarify.plot(sizeList,
              label=nameList,
              alpha=0.7)
plt.hsv()  # set color
plt.axis("off")
plt.show()
