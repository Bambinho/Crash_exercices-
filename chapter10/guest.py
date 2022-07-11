#a program that prompt the user to enter their name
name=input("Please Enter your name :")

filename='guest_book.txt'

with open(filename,'w') as file_object:
	file_object.write(name)
