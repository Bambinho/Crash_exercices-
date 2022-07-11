from random import choice

number=[12,23,76, 97,15,27,37, 92,63,84,'a','b','g','c','m']

def play():
	tickets=[]
	for select in range(1,5):
		tickets.append(choice(number))
	return tickets
 
print(f"Any ticket matching these four numbers or letters ( {play()} ) wins you a price")

my_ticket=[12,'a',27,'g']
my_ticket=play()

count=0
while True:
	count+=1
	if my_ticket==play():
		break

print(f"The loop has to run {count} times to give a winning tickets ")