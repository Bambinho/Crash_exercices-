sandwich_orders=['Chicken Sandwich', 'Egg Sandwich','Seafood Sandwich','Roast Beef Sandwich' ]
finished_sandwich=[] 

while sandwich_orders:

	sandwich=sandwich_orders.pop()
	print(f"I made your {sandwich.title()}")
	finished_sandwich.append(sandwich)


print("\nThe sandwich that were made are:")

for sandwich in finished_sandwich:
	print(f"\t{sandwich}")