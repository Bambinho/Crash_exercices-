#Making a user class 
class User:
	def __init__(self,first, last,city, country):
		self.first_name=first
		self.last_name=last 
		self.country=country
		self.city=city
		self.login_attempts=0

	def describe_user(self):
		print(f"The user full name is : {self.first_name.title()} {self.last_name.title()}")
		print(f"The user is from {self.country.title()} in the city named {self.city.title()}")

	def greet_user(self):
		print(f"\nHello, {self.first_name.title()} welcome to my page")

	def increment_login_attempts(self):
		self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0

# user1= User('Tiemoko','Bamba','Edmonton','Canada')

# user1.increment_login_attempts()
# print(f"The number of attemps was: {user1.login_attempts}")
# user1.increment_login_attempts()
# print(f"The number of attemps was: {user1.login_attempts}")
# user1.increment_login_attempts()
# print(f"The number of attempts was: {user1.login_attempts}")
# user1.reset_login_attempts()
# print(f"The number of attempts was: {user1.login_attempts}")

# user2=User('Laryn','Cameroun','Toronto','Canada')
# user2.greet_user()
# user2.describe_user()

# user3=User('Mohamed','Bamba','Bouake','Cote D ivoire')
# user3.greet_user()
# user3.describe_user()


