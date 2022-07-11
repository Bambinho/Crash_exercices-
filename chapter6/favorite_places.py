favorite_places={
    'tiemoko':['toronto','aouake','abidjan','massachousette'],
    'ezekiel':['bondoukou','calgary','edmonton'],
    'kader':['agboville','wagadougou',],
    }


for key, places in favorite_places.items():
	print(f"\n{key.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")
