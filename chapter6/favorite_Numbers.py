favorite_number={
	'Eze': [20,18 ,183 ,49, 484 , 74 ,48 ],
	'Tiemoko': [18,44,847,84,99,294,48],
	'Ines': [64,67,88,92,38,47,74,82,88,93],
	'Kader':[46,54,67,44,98,20,19,30,23,24,89,94],
	'Nullar':[37,47,78,22,92,90,43,94,84,8],
	}
for name, numbers in favorite_number.items():
	print(f"\n{name.title()}'s numbers are:")
	for number in numbers:
		print(f"\t{number}")

