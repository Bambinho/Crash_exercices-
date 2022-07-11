def count_words(filename):
	"""Count the approximate number of words in a file"""
	try:
		with open(filename) as f :
			contents=f.read()
	except FileNotFoundError:
			#print(f"Sorry, The file {filename} does not exist.")
			pass
	else :
			words=contents.split()
			num_word=len(words)
			print(f"The file {filename} has {num_word} words")



filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
	count_words(filename)