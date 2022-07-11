### writing a loop asking people why they wanna take asking people why they wanna take a survey
filename='poll.txt'
prompt='Enter your name: '
prompt1="Please The reason why you like programming: "
message='\n'
while True:
	with open(filename, 'a') as file_object:
		message=input(prompt)
		file_object.write(f"{message}: ")
		message=input(prompt1)
		file_object.write(f"{message}\n")


