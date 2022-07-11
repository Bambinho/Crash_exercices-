#Making a restaurant class and printing the attribute 
class Restaurant:
	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name=restaurant_name
		self.cusine_type=cusine_type
		self.number_served=0

	def describe_restaurant(self):
		print(f"The restaurant name is: {self.restaurant_name}")
		print(f"Our cusine type is: {self.cusine_type}")

	def open_restaurant(self):
		print("\nThe restaurant is open")

	def set_number_served(self,number):
		self.number_served=number
	def increment_number_served(self,number):
		self.number_served+=number




restaurant=Restaurant('Catsus','Occidental Cuisine')
print(f"The restaurant has served {restaurant.number_served} customer")
restaurant.number_served=25
print(f"The restaurant has served {restaurant.number_served} customer")

restaurant.set_number_served(30)
print(f"The restaurant has served {restaurant.number_served} customer")
restaurant.increment_number_served(60)
print(f"The restaurant has served {restaurant.number_served} customer today" )
# print(f"Le nom du restaurant est {restaurant.restaurant_name}")
# print(f"Le type de cusine est {restaurant.cusine_type}\n")

# restaurant.open_restaurant()
# restaurant.describe_restaurant()
