filename='learning_python.txt'

with open(filename) as file_object:
	print(file_object.read())

print("\n")
with open(filename) as file_object:
	#lines=file_object.readlines()
	for line in file_object:
		print(line.rstrip())

with open(filename) as file_object :
	lines=file_object.readlines()
print("\n")
for line  in lines:
	print(line.strip())