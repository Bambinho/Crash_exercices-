
#list of argument technique of calling function

# def describe_pet(animal_type, pet_name):
# 	""" Display information about pets."""
# 	print(f"\nI have a {animal_type}")
# 	print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet('dog','mary')
# describe_pet('cat','jhon')

#Keyword technique of calling function 

# def describe_pet(animal_type, pet_name):
# 	""" Display information about pets."""
# 	print(f"\nI have a {animal_type}")
# 	print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet(pet_name='harry',animal_type='hamster')

#Default Values 

def describe_pet(pet_name, animal_type='dog'):
	""" Display information about a pet"""
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")
# A dog name Billy
describe_pet('Billy')
describe_pet(pet_name='Billy')

# A hamster name Harry.
describe_pet('Harry','hasmter')
describe_pet(pet_name='harry')
describe_pet( animal_type='hamster',pet_name='Kane',)
