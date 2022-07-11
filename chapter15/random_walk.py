from random import choice 

class RandomWalk:
	"""A class to generate random walks"""

	def __init__(self,num_points=5000):
		"""Initialize attributes of walk"""
		self.num_points=num_points 

		#all walk start at (0,0)
		self.x_values=[0]
		self.y_values=[0]

	def fill_walk(self):
		"""Calculate the point of the walk"""
		## Keep taking steps untill the walk reaches the desired length.

		while len(self.x_values)<self.num_points:

			##Decide which direction to go and how far to go in that direction.
			x_direction=choice([-1,1])
			x_distance=choice([1,2,3,4])
			x_step=x_distance*x_direction 

			x=y_direction=choice([-1,1])
			y_distance=choice([1,2,3,4])
			y_step=y_distance*y_direction 

			if x_step==0 or y_step==0:
				continue
			#Calculate the new position 
			x=self.x_values[-1] +x_step
			y=self.y_values[-1] +y_step 

			self.x_values.append(x)
			self.y_values.append(y)







