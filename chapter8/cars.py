#Writing a function about car informations

def make_car(manufacture,model,**car_info):
	car_info['manufacture']=manufacture
	car_info['model']=model

	return car_info

car=make_car('subaru','outback',color='blue',tow_package=True,owner='zimbaba')

print(car)
car=make_car('pontiac','vibe',color='grew',owner='Tiemoko')
print(car)