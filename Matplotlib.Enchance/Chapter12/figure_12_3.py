import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap

class MapDisVisualization(Basemap):

    # get city names
    def getCityNames(self,names):
        namesKeys = list(names.keys())
        return namesKeys

    # define distance between cityA and cityB
    def citiesDistance(self,x,y):
        d = np.power(np.power(x[0]-y[0],2)+np.power(x[1]-y[1],2),0.5)
        distance = round(d,4)
        return distance

    # compute distance between target city and every other city
    def centerCityDistance(self,city,names):
        distanceDict = {}
        namesKeys = self.getCityNames(names)
        for i,name in enumerate(namesKeys):
            if name != city:
                distanceDict[name] = self.citiesDistance(names[city],names[name])
        return distanceDict

    # compute line width and line color
    def setcolorandwidth(self,city,names):
        size_factor = 2.0
        namesKeys = self.getCityNames(names)
        distanceDict = self.centerCityDistance(city,names)
        distanceList = list(distanceDict.values())
        maxDistance = max(distanceList)
        for i,name in enumerate(namesKeys):
            if name != city:
                self.drawgreatcircle(names[city][1],names[city][0],
                                     names[name][1],names[name][0],
                                     linewidth=size_factor,
                                     color=mpl.cm.Blues(distanceDict[name]/float(maxDistance)))

    # visualize city distance on the map
    def showmap(self,city,names):
        self.setcolorandwidth(city,names)
        namesKeys = self.getCityNames(names)
        number = len(namesKeys)
        titleContent = "a map of visualizing distance between %s and every other city (%d cities)"
        font = dict(family="serif",fontsize=15,weight="black")
        plt.title(titleContent % (city,(number-1)),fontdict=font)
        plt.show()

def main(projection,city):
    # get a Basemap instance
    m = MapDisVisualization(projection=projection,
                            resolution="h",
                            area_thresh=0.1,
                            llcrnrlon=112,llcrnrlat=-50,
                            urcrnrlon=180,urcrnrlat=-8)

    # draw several elements on the map
    m.drawcoastlines(linewidth=0.6,linestyle="-",zorder=2)
    m.fillcontinents(alpha=0.5,zorder=1)
    m.drawmapboundary(color="gray")
    m.drawmeridians(np.arange(100,180,15),linewidth=0.4,labels=[0,0,0,1])
    m.drawparallels(np.arange(-90,0,15),linewidth=0.4,labels=[1,0,0,0])
        
    # Latitude and Longitude in degrees
    names = {"Sydney":(-33.86785,151.20732),"Wellington":(-41.28664,174.77557),
             "Brisbane":(-27.46794,153.02809),"Adelaide":(-34.92866,138.59863),
             "Perth":(-31.95224,115.8614),"Auckland":(-36.86667,174.76667),
             "Darwin":(-12.46113,130.84185),"Canberra":(-35.28346,149.12807)}

    #show the distance between Sydney and every other city
    m.showmap(city,names)

if __name__ == "__main__":
    # use projection mercator and choose Sydney
    main("merc","Sydney")
