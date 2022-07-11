#Collectig what a person want on a sandwich 

def sandwiches(*toppings):
	print("\n The summary of the items you wants on your sandwiche are:")
	for topping in toppings:
		print(f"\t-{topping.title()}")

sandwiches('tomatoes')
sandwiches('tomatoes','onions','mushroom')

sandwiches('onions','mushroom')

sandwiches('tomatoes','onions','mushroom','carbage')

