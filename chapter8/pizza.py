def make_pizza(size,*toppings):
	"""Print the list of topping that have been requested"""
	print(f"\nMaking a {size}-inch pizza with the following toppings: ")
	for topping in toppings:
		print(f"-{topping}")

# make_pizza(12,'peperoni')
# make_pizza(16,'mushroom','green peppers','extra cheese')

