from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
	""" Model for the pizzas """
	name=models.CharField(max_length=10)
	date_added=models.DateTimeField(auto_now_add=True)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Topping(models.Model):
	"""Model for the Toppings """
	pizza=models.ForeignKey(Pizza,on_delete=models.CASCADE)
	name=models.CharField(max_length=10)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self) :
		return self.name




