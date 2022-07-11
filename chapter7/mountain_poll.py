##Filling a dictionary with User Input

responses={}
#Set a flag to indicate that pollings active 
polling_active=True

while polling_active :
	#Prompt for the person's name and response 
	name=input("\nWhat is your name ?")
	response=input("Which mountain would you like to climb someday ?")

	#Store the response in a dictionary 
	responses[name]=response

	#Find out if annyone else is going to take the poll.
	repeat=input("Would you like to let another person respond?(yes/no)")
	if repeat=='no':
		polling_active=False

#Polling is complete.Show the results 

print("\n---Poll Result---")

for name, response in responses.items():
	print(f"\n {name.title()} would like to climb {response}")

