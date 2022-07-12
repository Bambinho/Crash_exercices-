from django.db import models

# Create your models here.

class Pizza(models.Model):
	""" Model for the pizzas """
	name=models.CharField(max_length=10)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Topping(models.Model):
	"""Model for the Toppings """
	pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
	name=models.CharField(max_length=10)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self) :
		return self.name




