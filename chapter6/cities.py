cities={
	'bouake':{'country':'ivory coast','population':530_000 ,'fact':'This is my home city'},
	'abidjan':{'country':'ivory coast','population':4_300_000,'fact':'This my capital city'},
	'edmonton':{'country':'canada','population':980_000,'fact':"This the city where I am currently living right now"},
}

for name, infos in cities.items():
	print(f"\nThe information about {name.title()} are:")
	for info,descript in infos.items():
		if  info=='country':
			print(f"\t{info.title()}: {descript.title()}")
		else :
			print(f"\t{info.title()}: {descript}")
