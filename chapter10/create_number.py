import json

def create_number():
	filename='number.json'
	number=input("Please Enter Your favorite Number? ")
	with open(filename,'w') as f:
		json.dump(number,f)
	return number 



