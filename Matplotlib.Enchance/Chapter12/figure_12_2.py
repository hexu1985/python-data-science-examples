import datetime
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

# setup miller projection
basemap = Basemap(projection="mill",
                  resolution="h",
                  area_thresh=0.1,
                  llcrnrlon=-180,
                  llcrnrlat=-90,
                  urcrnrlon=180,
                  urcrnrlat=90)

# draw coastlines
basemap.drawcoastlines(linewidth=0.6,zorder=2)
# draw mapboundary
basemap.drawmapboundary(fill_color="aqua")
# fill continents with color "coral", and lake "aqua"
basemap.fillcontinents(color="coral",lake_color="aqua",zorder=1)
# draw meridians and parallels
basemap.drawmeridians(np.arange(-120,150,60),linewidth=0.6,labels=[0,0,0,1])
basemap.drawparallels(np.arange(-60,80,30),linewidth=0.6,labels=[1,0,0,0])

# shade the night areas, and use current time in UTC
date = datetime.datetime.utcnow()
basemap.nightshade(date)

# format title with date and time
content = "Shade dark regions of the map %s (UTC)"
dtFormat = "%d %b %Y %H:%M:%S"
stringTime = date.strftime(dtFormat)
plt.title(content % stringTime,fontsize=15)

plt.show()
