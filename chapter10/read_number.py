import json

def read_number():
	filename='number.json'
	try:
		with open(filename) as f :
			number=json.load(f)
	except FileNotFoundError:
		number=None
	else:
		return number
	