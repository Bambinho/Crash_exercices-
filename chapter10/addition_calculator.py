#exception about numbers 
#a=int(input("input a first number to be added: "))
while True:

	try :
		a=int(input("\ninput a first number to be added: "))
	except ValueError :
		print("The first number you entered is not a numbr")
		continue 

	try :
		b=int(input("Please input a second number: "))
	except ValueError :
		print("The second number you have entered is not a number")
	else :
		print(f" The result of the additon of the two numbers are: {a+b}")



