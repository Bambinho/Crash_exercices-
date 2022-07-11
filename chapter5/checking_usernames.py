current_users=['Tiemoko','bamba','jean','Paul','gauloir','micheal']
new_users=['mariam','bile','rene','tiemoko','ben','Jean','badi']
existing_users=[use.lower() for use in current_users ]
for user in new_users:
	if user.lower() in existing_users:
		print('You need to enter a new user name.')
	else:
		print('The username is Available.')
