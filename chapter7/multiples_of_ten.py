number=input("Please input a number? ")
number=int(number)

if number%10:
	print(f"{number} is not a multiple of 10")
else:
	print(f"{number} is a multiple of 10")