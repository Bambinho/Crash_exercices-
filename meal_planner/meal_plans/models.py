from django.db import models

# Create your models here.

class Day(models.Model):
	""" Day of the week """
	day_name=models.CharField(max_length=10)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):


		return self.day_name

class Meal(models.Model):
	"""Meals of the day """
	day=models.ForeignKey(Day,on_delete=models.CASCADE,default=True)
	meal_name=models.CharField(max_length=10)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):

		return self.meal_name


