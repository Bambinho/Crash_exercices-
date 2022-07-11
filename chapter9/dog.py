class Dog:
	""" A simple attend to model a dog"""
	def __init__(self, name,age):
		"""Intialize name and age attributes."""
		self.age=age 
		self.name=name

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now siting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog=Dog('Willie',6)
your_dog=Dog('Lucie',3)
print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old")
my_dog.sit()

print(f"\nYour dog name is {your_dog.name}")
print(f"Your dog is {your_dog.age}")

your_dog.sit()