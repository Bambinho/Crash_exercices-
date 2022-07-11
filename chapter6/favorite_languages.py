# favorite_languages={
# 	'jen':'python',
# 	'sarah':'c',
# 	'edward':'ruby',
# 	'phil':'python',
# 	}

favorite_languages={
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
	}

#language=favorite_languages['sarah'].title()

#print(f"Sarah's favorite language is {language}")


#Lopping through all key-value pair
#for name, language in favorite_languages.items():
	#print(f"\n{name.title()}'s favorite language is {language.title()}")


#loopping through all the keys in a dictionary

#for name in favorite_languages.keys():
	#print(name.title())

#friends=['phil','sarah']

#for name in favorite_languages.keys():
	#print(f"Hi {name.title()}")
	#if name in friends:
		#language=favorite_languages[name].title()
		#print(f"\t{name.title()},I see you love {language}!")
#if 'erin' not in favorite_languages.keys():
	#print("Erin, please take our poll!")

#Looping through a Dictionary key in particulary order
#for name in sorted(favorite_languages.keys()):
	#print(f"{name.title()},thank you for taking the poll.")

#Looping through all values in a Dictionary 

# print ("The following language have been mentioned:")
# for language in set(favorite_languages.values()):
# 	print(language.title())

for name, languages in favorite_languages.items():
	if len(languages)==1:
		print(f"{name.title()}'s favorite language is {languages[0].title()}")
	else:
		print(f"{name.title()}'s favorite language are:")
		for language in languages:
			print(f"\t{language}")
