import json
import read_number
import create_number

number=read_number.read_number()

if number:
	print(f"I know yoru favorite number! it is {number}")
else:
	number=create_number.create_number()
	print(f" We will remember your favorite number when you are back !")
