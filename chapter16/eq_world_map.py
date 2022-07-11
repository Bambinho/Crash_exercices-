import json 
from plotly.graph_objs import Scattergeo,Layout

from plotly import offline 

filename='/home/timlinux/Downloads/crash_course/chapter16/data/eq_data_30_day_m1.json'

with open(filename) as f:
	all_eq_dict=json.load(f)

eq_list=all_eq_dict['features']

mags,lons,lats,hover_texts=[],[],[],[]

for eq_dict in eq_list:

	mag=eq_dict['properties']['mag']
	lon=eq_dict['geometry']['coordinates'][0]
	lat=eq_dict['geometry']['coordinates'][1]
	title=eq_dict['properties']['title']
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hover_texts.append(title)

data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},
    }
    }]

layout=Layout(title='Plot of Earthquake')

fig={'data':data, 'layout':layout}

offline.plot(fig)


