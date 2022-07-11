import json 

# #username=input ("What is your name? ")
# filename='username.json'
# try:
# 	with open(filename) as f :
# 		username=json.load(f)
# except FileNotFoundError :
# 	username=input('What is your name? ')
# 	with open(filename,'w') as f :
# 		json.dump(username,f)
# 		print(f"We will remember you when you come back,{username}")
# else :
# 	print(f"Welcome back,{username}")
# 	

def get_stored_username():
	"""Get storeed username if available """
	filename='username.json'
	try:
		with open(filename) as f :
			username=json.load(f)
	except FileNotFoundError:
		username=None
	else:
		return username


def create_user():
	""" prompt for a new username """
	username=input("Please enter a user name : ")
	filename='username.json'
	with open(filename,'w') as f :
		json.dump(username,f)
	return username

def check_name(username):
	"""Check if the username already exist"""
	check_name=input(f"Is {username} your username?(y) ")
	if check_name=='y':
		print(f"Welcome back,{username}")
		
	else :
		username=create_user()

		


def greet_user():
	"""Greet user  by username ."""
	username=get_stored_username()
	if username:
		# check_name=input(f"Is {username} your username?(Y,N)")
		# if checkname=='y':
		# 	print(f"Welcome back,{username}")
		# elif checkname=='n':
		# 	username=create_user()
		check_name(username)
	else:
		username=create_user()
		print(f"We will remember you when you are back,{username}")

greet_user()

