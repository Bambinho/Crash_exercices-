prompt="\nEnter a pizza topping? "
message=""
while message!='quit':
	message=input(prompt)
	print(f"I will {message.title()} to the pizza")