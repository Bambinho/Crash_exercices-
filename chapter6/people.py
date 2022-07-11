person1={
	'first':'Ines',
	'last' : 'Kouame',
	'age'       :21,
	'city'      : 'Edmonton',
	}
person2={
    'first':'Eze',
    'last':'Koffi',
    'age':25,
    'city':'galgary',
    }

person3={
	'first':'mason',
	'last':'mount',
	'age':23,
	'city':'london'
}

people=[person1,person2,person3]

for person in people:
	print(f"\nFullname: {person['first'].title()} {person['last'].title()}")
	print(f"\tAge: {person['age']}")
	print(f"\tCity: {person['city']}")

