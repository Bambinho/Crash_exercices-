places={}
prompt='If you could visit one place in the world, where would you go? '
flag=True

while flag :
	user=input("What is your name :")
	place=input(prompt)

	places[user]=place 

	repeat=input("Would you like to let another person respond?")
	if repeat=='no':
		flag=False 

print("\n---The Result of The Pool---")

for user, place in places.items():
	print(f"{user.title()} would like to go to {place}")
