filename='learning_python.txt'

with open(filename) as file_object:
	lines=file_object.readlines()


for line in lines:
	message=line.strip()
	message=message.replace('python','C')
	#stin.replace('python','c')
	print(message)

