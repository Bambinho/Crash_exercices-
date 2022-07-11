import json 
from math import*

from plotly.graph_objs import Layout, Scattergeo
from plotly import offline 

filename='/home/timlinux/Downloads/crash_course/chapter16/data/all_month.json'

with open(filename) as f:
	eq_data=json.load(f)

filename='/home/timlinux/Downloads/crash_course/chapter16/data/readable_all_month.json'

with open(filename,'w') as f :

	json.dump(eq_data,f,indent=4)

with open(filename) as f:

	eq_data=json.load(f)

mags,lons,lats,texts=[],[],[],[]
eq_dicts=eq_data['features']
for eq_dict in  eq_dicts:
	mags.append(eq_dict['properties']['mag'])
	lons.append(eq_dict['geometry']['coordinates'][0])
	lats.append(eq_dict['geometry']['coordinates'][1])

for i,value in enumerate(mags):
	try:
		float(value)
	except TypeError:
		print('Error',i)
		mags[i]=0
#print(len(mags),len(lons),len(lats))
# data=[{
# 	  'type':'scattergeo',
# 	  'lon':lons,
# 	  'lat':lats,
# 	  'marker':{
# 	      'size':[3*int(mag) for mag in mags],
	    
# 	      }
# 	 }]
data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    #'text':hover_texts,
    'marker':{
        'size':[3*abs(mag) for mag in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'},
    }
    }]



layout= Layout(title=" Prototype")

offline.plot({'data':data,'layout':layout})


