prompt="\nPlease Enter your age: "
prompt+="\n(Enter quit to quit) "

message=""

flag=True
while flag:
	message=input(prompt)
	if message=='quit':
		break
	message=int(message)
	if int(message) <3 :
		print("The ticket is free")
	elif message < 12:
		print("The ticket cost $10")
	elif message >=12 :
		print("The ticket cost $15")
