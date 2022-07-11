#message=input("Tell me something, I will repeat it back to you: ")

#print(message)

prompt="\nEnter something, and I will repeat it back to you: "
prompt+="\nEnter 'quit' to end the program. "
activate=True
message=""
while message != 'quit':
	message=input(prompt)

	if message !='quit':
		activate=False
	else:
		print(message)
