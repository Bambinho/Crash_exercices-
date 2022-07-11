rivers={
    'nile':'egypte',
    'missipi':'United State',
    'yangtze':'china',
    'amazon':'brasil',
    }

for key, value in rivers.items():
	print(f"The {key.title()} run through the {value}")
print("\n\n")
for key in rivers.keys():
	print(f"{key}")
print("\n\n")
for value in rivers.values():
	print(f"{value}")
