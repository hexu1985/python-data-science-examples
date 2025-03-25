from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# city population in 2017
locations = {"Sydney":5131326,"Melbourne":4850740,
             "Brisbane":2408223,"Adelaide":1333927,
             "Perth":2043138,"Hobart":226884,
             "Darwin":146612,"Canberra":410301}

# Latitude and Longitude in degrees
names = {"Sydney":(-33.86785,151.20732),"Melbourne":(-37.8142,144.96332),
         "Brisbane":(-27.46794,153.02809),"Adelaide":(-34.92866,138.59863),
         "Perth":(-31.95224,115.8614),"Hobart":(-42.87936,147.32941),
         "Darwin":(-12.46113,130.84185),"Canberra":(-35.28346,149.12807)}

# setup mercator map projection
basemap = Basemap(projection="merc",
              resolution="h",
              area_thresh=0.1,
              llcrnrlon=112,llcrnrlat=-45,
              urcrnrlon=155,urcrnrlat=-8)

# draw several map elements
basemap.drawcoastlines(linewidth=0.6,linestyle="-",color="#b7cfe9",zorder=3)
basemap.drawrivers(linewidth=0.8,linestyle="-",color="#689CD2",zorder=2)

basemap.fillcontinents(color="#BF9E30",lake_color="#689CD2",zorder=1)
basemap.drawmapboundary(color="gray",fill_color="#689CD2")

basemap.drawmeridians(np.arange(0,360,15),color="#4e8bca",labels=[0,0,0,1],labelstyle="+/-")
basemap.drawparallels(np.arange(-90,90,15),color="#4e8bca",labels=[1,1,0,0],labelstyle="+/-")


# convert lon/lat (in degrees) to x/y map projection coordinates (in meters)
# longitude is transformed into x and latitude is transformed into y
names_values = []
names_keys = list(names.keys())
for i,name in enumerate(names_keys):
    names_values.append(names[name])

lat_x,long_y = list(zip(*names_values))
x,y = basemap(long_y,lat_x)

# draw city markers and add text to markers
size_factor = 80.0
offset_factor = 21000
rotation = 30
max_population = max(locations.values())

for city_name,city_x,city_y in zip(names_keys,x,y):
    size = (size_factor/max_population)*locations[city_name]
    x_offset = offset_factor
    y_offset = offset_factor
    basemap.scatter(city_x,
                    city_y,
                    s=size,
                    facecolor="w",
                    edgecolors="r",
                    linewidths=2.0,
                    zorder=10)
    plt.text(city_x+x_offset,city_y+y_offset,city_name)

# setup map title
font = dict(family="serif",fontsize=15,weight="bold")
plt.title("Australian Population of Capital City",**font)

plt.show()
