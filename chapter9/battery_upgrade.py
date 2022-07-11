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

class Battery:
	""" A simple attempt to mode a battery for an Electric car."""

	def __init__(self,size=75):
		"""Initialize the battery's attributes."""
		self.battery_size=size

	def describe_battery(self):
		"""Print a statement describing the battery"""
		print(f"This car has a {self.battery_size}--kwh battery.")

	def get_range(self):
		"""Print a statement about the rang this battery provide"""
		if self.battery_size==75:
			rang=260
		elif self.battery_size==100:
			rang=315
		else:
			rang=300
		print(f"This car can go about {rang} on a full charge.")

	def upgrade_battery(self):
		if self.battery_size!=100:
			self.battery_size=100

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles"""
	def __init__(self,make, model, year):
		"""Initialize attribute of parents class"""
		super().__init__(make,model,year)
		self.battery_size=75 
		self.battery= Battery()

	# def describe_battery(self):
	# 	"""print a statement describing the battery"""
	# 	print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
