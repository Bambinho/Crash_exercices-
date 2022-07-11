from random import choice

number=[12,23,76, 97,15,27,37, 92,63,84,'a','b','g','c','m']

def play():
	tickets=[]
	for select in range(1,5):
		tickets.append(choice(number))
	return tickets
 
print(f"Any ticket matching these four numbers or letters ( {play()} ) wins a price")
