"""A class that can be used to represent a car"""
class Car:
	"""A simple attempt to represent a car."""
	def __init__(self,make, model, year):
		self.make=make 
		self.model=model
		self.year=year
		self.odometer=0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometer(self):
		"""Print a statement showing the car millage"""
		print(f"This car has {self.odometer} mile on it.")
	def update_odometer(self,mileage):
		"""update the value of the odometer"""
		if mileage>= self.odometer:
			self.odometer=mileage
		else:
			print("You can't roll back the odometer")
	def increment_odometer(self,miles):
		"""Add the given amount to the odometer reading"""
		self.odometer+=miles 

# class Battery:
# 	"""A simple attempt to model a battery for an electric car """
# 	def __init__(self, battery_size=70):
# 		"""Initilize the battery attribute"""
# 		self.battery_size=battery_size
# 	def describe_battery(self):
# 		"""Print a statement about the range this battery has"""
# 		print(f"This car has a {self.battery_size}-kwh battery")
# 	def get_range(self):
# 		"""Print a statement a range the range this battery provides"""
# 		if self.battery_size==75:
# 			range=260
# 		elif self.battery_size==100:
# 			range=315
# 		else:
# 			range=300

# 		print(f"This battery can go about {range} mile on a full charge.")

# class ElectricCar(Car):
# 	""" Model aspect of car specific to electric car"""
# 	def __init__(self,make, model, year):
# 		""" Initilize attribute for the parent class
# 		 then the attribute of the child class"""
# 		super().__init__(make, model, year)
# 		self.battery=Battery()







# my_used_car=Car('subaru','outback',2015)
# print(my_used_car.get_descriptive_name())

# # my_new_car.odometer=23
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()