def get_formated_name(first_name,last_name,middle_name=''):
	""" Return a full name neatly formatted"""
	if middle_name:
		full_name=f"{first_name} {middle_name} {last_name}"
	else :
		full_name=f"{first_name} {last_name}"
	return full_name.title()

musician=get_formated_name('eze','koffi','belize')

print(musician)

programer=get_formated_name('Tiemoko','Bamba')

print(programer)

