#usernames=['tiemoko','admin','tatinda','eze','ines']
usernames=[]
if usernames:
	for username in usernames:
		if username== 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print(f'Hello {username}, thank you for logging again.')
else:
	print('We need to find more users!')
