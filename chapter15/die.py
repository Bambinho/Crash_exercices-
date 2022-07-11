from random import randint 

class Die:
	""" A class representing a single die."""
	def __init__(self,num_sides=6):
		"""Assume the die has 6 sides """
		self.num_sides=num_sides 

	def roll(self):
		"""Return the number when the die roll"""
		return randint(1,self.num_sides)