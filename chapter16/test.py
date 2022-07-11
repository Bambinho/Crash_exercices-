import recent_earth_quakes as eq 

print(eq.mags[:10])
print(len(eq.mags))
for i,value in enumerate(eq.mags):
	try:
		float(value)
	except TypeError:
		print('Error',i)
		eq.mags[i]=0

print('\n\n\n')
for i,value in enumerate(eq.mags):
	try:
		float(value)
	except TypeError:
		print('Error',i)
		eq.mags[i]=0
