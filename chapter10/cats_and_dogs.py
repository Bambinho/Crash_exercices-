###Wite a function to oepn files and check if there is a file not found error 

filename='dogs.txt'

def open_textfile(filename):
	with open(filename) as f:
		contents=f.read()
		print(contents)
filenames=['dogs.txt','cat.txt']

for filename in filenames:
	try:
		open_textfile(filename)
	except FileNotFoundError:
		pass 
		#print(f"The file {filename} can't be found.")


