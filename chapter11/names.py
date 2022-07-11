from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")

while True:
	first=input("Please give your first name: ")
	if first=='q':
		break
	last=input("Please give your last name: ")
	if last=='q':
		break 

	full_name=get_formatted_name(first,last)
	print(f"\nNeatly formatted name: {full_name}")
	
