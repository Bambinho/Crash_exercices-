#Making a restaurant class and printing the attribute 
class Restaurant:
	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name=restaurant_name
		self.cusine_type=cusine_type

	def describe_restaurant(self):
		print(f"The restaurant name is: {self.restaurant_name}")
		print(f"Our cusine type is: {self.cusine_type}\n")
	def open_restaurant(self):
		print("\nThe restaurant is open")

restaurant=Restaurant('Catsus','Occidental Cuisine')
restaurant.describe_restaurant()
# print(f"Le nom du restaurant est {restaurant.restaurant_name}")
# print(f"Le type de cusine est {restaurant.cusine_type}\n")

restaurant1=Restaurant('MacDonalds','Junk Food')
restaurant1.describe_restaurant()
restaurant2=Restaurant('Earls','occidental Cuisine')
restaurant2.describe_restaurant()


