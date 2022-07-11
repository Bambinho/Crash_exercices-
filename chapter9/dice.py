from random import randint

class Dice:
	""" Making a class dice with an attribute sides"""
	def __init__(self,sides=6):
		self.sides=sides

	def roll_die(self):
		print(f" You played {randint(1,self.sides)} " )


dice_6_side=Dice()

for play in range(10):
	dice_6_side.roll_die()

dice_10_side=Dice(10)
print("\n")
for play in range(10):
	dice_10_side.roll_die()
print("\n")
dice_20_side=Dice(20)
print("\n")
for play in range(10):
	dice_20_side.roll_die()







