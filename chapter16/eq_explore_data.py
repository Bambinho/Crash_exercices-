import json 
##explore the structure of the data 
filename='/home/timlinux/Downloads/crash_course/chapter16/data/eq_data_1_day_m1.json'

with open(filename) as f :
	all_eq_data=json.load(f)


all_eq_dict=all_eq_data['features']

print(len(all_eq_dict))

mags, lons,lats=[],[],[]

for eq_dic in all_eq_dict:

	mag=eq_dic['properties']['mag']
	lon=eq_dic['geometry']['coordinates'][0]
	lat=eq_dic['geometry']['coordinates'][1]

	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])


