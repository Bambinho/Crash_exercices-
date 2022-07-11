#Making a restaurant class and printing the attribute 
class Restaurant:
	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name=restaurant_name
		self.cusine_type=cusine_type

	def describe_restaurant(self):
		print(f"The restaurant name is: {self.restaurant_name}")
		print(f"Our cusine type is: {self.cusine_type}")
	def open_restaurant(self):
		print("\nThe restaurant is open")

class IceCreamStand(Restaurant):
	"""This class inherits from the restaurant class """
	def __init__(self, restaurant_name,cusine_type):
		super().__init__(restaurant_name,cusine_type)
		self.flavors=['banana','lemon','vanilla','mango']

	def show_flavors(self):
		"""This methode  showes the flavor of the Icecreams"""
		print("The flavor of the icecream are: ")
		for flavor in self.flavors:
			print(f"{flavor.title()}")

cream= IceCreamStand('Catsus','Ice cream')

cream.show_flavors()
