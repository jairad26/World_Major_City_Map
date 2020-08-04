import folium
import pandas as pd

data = pd.read_csv("worldcities.csv")
data.dropna(axis = 0)
population = list(data["population"])
lat = list(data["lat"])
lon = list(data["lng"])
city = list(data["city"])
country = list(data["country"])

html = """<h4>City information:</h4>
%s million
"""

def color_producer(population):
    if(2000000.0 <= population < 4000000.0):
        return 'orange'
    elif(4000000.0 <= population < 6000000.0):
        return 'red'
    else:
        return 'darkred'

map = folium.Map(location = [38.58, -99.09], zoom_start=2, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map") 


for lt, ln, pop, ci, coun in zip(lat,lon, population, city, country):
    if(pop >= 2000000.0):  
        popname = ci + ", " + coun + "\n" + "Population: " + str(round(pop/1000000.0,2))
        iframe = folium.IFrame(html=html % popname, width = 180, height = 115)
        fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 10, popup = folium.Popup(iframe), fill_color = color_producer(pop), color = 'grey', fill_opacity = 0.75))


map.add_child(fg)
map.save("Map1.html")