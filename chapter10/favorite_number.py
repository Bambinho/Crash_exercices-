import json 

filename='number.json'
number=input("Please Enter Your favorite Number? ")
with open(filename,'w') as f:
	json.dump(number,f)



