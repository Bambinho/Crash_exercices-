#Making a user class 
# class User:
# 	def __init__(self,first, last,city, country):
# 		self.first_name=first
# 		self.last_name=last 
# 		self.country=country
# 		self.city=city
# 		self.login_attempts=0

# 	def describe_user(self):
# 		print(f"The user full name is : {self.first_name.title()} {self.last_name.title()}")
# 		print(f"The user is from {self.country.title()} in the city named {self.city.title()}")

# 	def greet_user(self):
# 		print(f"\nHello, {self.first_name.title()} welcome to my page")

# 	def increment_login_attempts(self):
# 		self.login_attempts+=1
# 	def reset_login_attempts(self):
# 		self.login_attempts=0

from users import User 
class Privileges:
	def __init__(self):
		self.privileges=['can add a post','can delete a post','can send email to a user','can ban a user']

	def show_privileges(self):
		print("The privileges of an Admin are: ")
		for privilege in self.privileges:
			print(f"{privilege}")


class Admin(User):

	def __init__(self,first, last, city, country):
		super().__init__(first, last, city, country)
		self.privileges=Privileges()


# admin=Admin('Tiemoko','Bamba','Edmonton','Cote d ivoire')
# admin.privileges.show_privileges()
