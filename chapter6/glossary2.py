glossary={
    'methode': 'A methode is function that modify some property of an object(list, sting or even dictionary)',
	'list': 'A list is an entity to store data',
	'tuple': 'A tuple is like a list but we cam modify an element of a list',
	'loop':'A loop help goes through element of a list or dictionary',
	'if_statement':'An if statement helps makes decissions',
	}

#print(f"Methode:      {glossary['methode']}\n")

for key, value in glossary.items():
	print(f"{key.title()} : {value}")
glossary['set']='A set is defined as a dictionary but act as like a list'
glossary['interpreter']='An interpreter is the app that runs python code when you press the run button'
glossary['key']=' In a dictionary we use a key to retrieve a value '
glossary['iterate']='To iterate mean to go through the element of a list, diction or set'
glossary['print']='To print mean to display the element of a set to the screen'
print("\n\n")
for key,value in glossary.items():
	print(f"{key.title()}: {value}")