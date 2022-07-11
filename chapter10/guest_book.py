###Write a that prompts the users for their name and print a greeting message to the user 

filename='guest_book.txt'
prompt='Please Enter your name: '
message=''
while True:
	with open(filename,'a') as file_object:
		message=input(prompt)
		print(f"Hello, {message.title()}")
		file_object.write(f"{message}\n")

