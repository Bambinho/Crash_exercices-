filenames=['davinci.txt','lacplace.txt','relativity.txt','pointcarre.txt']

def analyse(filename):

	try: 
		with open(filename) as f :
			contents=f.read()
	except FileNotFoundError:
		print(f"The file {filename} could not be found")
	else: 
		print(f"We have found {contents.lower().count('the')} appearance of (the) in {filename}")

for file in filenames:
	analyse(file)



