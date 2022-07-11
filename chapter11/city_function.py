
def get_formatted_place(city,country,population=''):

	if population:
		place=f"{city.title()}, {country.title()}- population {population}"

	else :
		place=f"{city.title()}, {country.title()}"

	return place

# place=get_formatted_places('edmonton','canada')
# print(place)


