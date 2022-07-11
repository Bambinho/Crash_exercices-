import csv
from math import*

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline 



##Calculate the distance between two given cities
EARTH_R=6371
def get_distance(lat1,lon1,lat2,lon2):

	return (acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(lon2-lon1))*EARTH_R)
#print(get_distance(-23.5504,-46.6339,30.0561,31.2394))

###Calculate the distance betwwen successive cities

filename='/home/timlinux/Downloads/coding_challenge/destinations.csv'

distance=[]
cities=[]
new_cities=[]
new_distance=[]
order_city=[]
cities_to_look=[]

with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
	for index, column_header in enumerate(header_row):
		print(index,column_header)
	for row in reader:
		cities.append(row[:])
#print(cities)
#print(len(cities))

#print(cities[1:])

##Finding the shortestpath between two given cities
def shortest_city(temp,New_cities):
	Distance=[]
	#print(f'this is the tmep{temp}')
	for city in New_cities :
		#print(f'\n {city}')
		Distance.append(get_distance(float(temp[2]),float(temp[3]),float(city[2]),float(city[3])))
	#print(distance)
	#print(min(Distance),Distance.index(min(Distance)))
	name_of_city=New_cities[Distance.index(min(Distance))]
	value=[min(Distance),name_of_city]
	
	return value







#getting the shortest city
cities_to_look=cities[1:]
new_cities.append(cities[0])
close_to_node=shortest_city(cities[0],cities_to_look)
#print(f'\n\n\n\nThis is the closing nose{close_to_node}\n\n')
node_pos=cities_to_look.index(close_to_node[1])
#print(f'\n\n This is the Mode pose {node_pos}\n\n')

Node=list(cities_to_look.pop(node_pos))
new_cities.append(Node)
new_distance.append(close_to_node[0])
#print(f'\n\nThis is the nnnnnnode {Node}\n\n')

while cities_to_look:
	close_to_node=shortest_city(Node,cities_to_look)
	node_pos=cities_to_look.index(close_to_node[1])
	Node=cities_to_look.pop(node_pos)
	new_cities.append(Node)
	#print(f'{new_cities}')
	new_distance.append(close_to_node[0])

last_distance=get_distance(float(cities[0][2]),float(cities[0][3]),float(new_cities[len(new_cities)-1][2]),float(new_cities[len(new_cities)-1][3]))
new_cities.append(new_cities[0])
new_distance.append(last_distance)

#print(cities)
#print(sum(new_distance))
#print(new_cities[len(new_cities)-1])
#print(new_cities[0])
#print(new_cities)
#print(new_distance)
#print(len(new_distance))
#print(len(new_cities))

###Plotting the The city visited 

lons,lats=[],[]
for city in new_cities:
	#print(f"{city[0].title()},{city[1].title()} {city[2]} {city[3]}")
	lons.append(city[3])
	lats.append(city[2])

print(f"{sum(new_distance)}")
hover_text=[ f"city number {i}\n( {new_cities[i][0]},{new_cities[i][1]} )" for i, n in enumerate(new_cities) ]


data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_text,
    'marker':{
        'size':[ 6 for i in new_cities],
        'color':[i for i, n in enumerate(new_cities)],
        'colorbar':{'title':'City visited from first city (dark blue) to last city (dark yellow)'},
    },

	}]

layout=Layout(title='Coding challenge graph')

fig={'data':data, 'layout':layout}

offline.plot(fig)





tps://hacker-news.firebaseio.com/v0/item/19155826.json