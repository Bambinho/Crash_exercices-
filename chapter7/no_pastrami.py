sandwich_orders=['Chicken Sandwich','pastrami', 'Egg Sandwich','Seafood Sandwich','pastrami','Roast Beef Sandwich' ,'pastrami']
finished_sandwich=[] 

print("The deli has run out of pastrami\n")

while 'pastrami' in sandwich_orders:

	sandwich_orders.remove('pastrami')

while sandwich_orders:

	sandwich=sandwich_orders.pop()
	print(f"I made your {sandwich.title()}")
	finished_sandwich.append(sandwich)


print("\nThe sandwich that were made are:")

for sandwich in finished_sandwich:
	print(f"\t{sandwich}")