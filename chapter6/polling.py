favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
pool_people=['tiemoko','jen','phil','bamba']

for people in pool_people :
	if people in favorite_languages.keys():
		print("Thank you for responding!")
	else:
		print("You should take the pool")