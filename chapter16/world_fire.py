import csv 
from plotly.graph_objs import Layout,Scattergeo 
from plotly import offline 
from math import*

filename='/home/timlinux/Downloads/crash_course/chapter16/data/world_fires_1_day.csv'
with open(filename) as f :

	reader=csv.reader(f)
	header_row=next(reader)
	#print(header_row)
	lats,lons,brights=[],[],[]
	for row in reader:
		lats.append(row[0])
		lons.append(row[1])
		brights.append(row[2])
print (brights[:30])

for i, value in enumerate(brights):
	try:
		brights[i]=float(value)
	except ValueError:
		print('error')


data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[float(bright)/50 for bright in brights],
        'color':brights,
        'colorscale':'Viridis',
        'colorbar':{'title':'Brightness'}

    }
}]

layout=Layout(title='Graph of fire')

offline.plot({'data':data,'layout':layout})

