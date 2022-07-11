from random import choice 

class RandomWalk:
	"""A class to generate random walks"""

	def __init__(self,num_points=5000):
		"""Initialize attributes of walk"""
		self.num_points=num_points 

		#all walk start at (0,0)
		self.x_values=[0]
		self.y_values=[0]

	def get_step(self):
		direction=choice([-1,1])
		distance=choice([1,2,3,4,5])
		coordinate=direction*distance
		return coordinate

	def fill_walk(self):
		"""Calculate the point of the walk"""
		## Keep taking steps untill the walk reaches the desired length.

		while len(self.x_values)<self.num_points:

			##Decide which direction to go and how far to go in that direction.
			
			x_step=self.get_step()
			y_step=self.get_step() 

			if x_step==0 or y_step==0:
				continue
			#Calculate the new position 
			x=self.x_values[-1] +x_step
			y=self.y_values[-1] +y_step 

			self.x_values.append(x)
			self.y_values.append(y)







