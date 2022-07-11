pet_0={'animal':'dog','owner':'siata'}
pet_1={'animal':'cat','owner':'Ben'}
pet_2={'animal':'pigeon','owner':'Tiemoko'}
pet_3={'animal':'fish','owner':'mikayla'}
pet_4={'animal':'snake','owner':'lili'}

pets=[pet_0,pet_1,pet_2,pet_3,pet_4]

for pet in pets:
	print(f"\n{pet['owner'].title()} has a {pet['animal'].title()} as a pet")