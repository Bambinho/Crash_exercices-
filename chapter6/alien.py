#alien_0={'color':'green','points':5}

#new_points=alien_0['points']
#print(f'You just earned {new_points} points!')
#print(alien_0)
#alien_0['x_position']=0
#alien_0['y_position']=25
#print(alien_0)

#alien_0={}
#alien_0['color']='green'
#alien_0['points']=5
#print(alien_0)


#Modifying values in a dictionary
#alien_0={'color':'green'}
#print(f"The alien is {alien_0['color']}")
#alien_0['color']='yellow'
#print(f"The alien is now {alien_0['color']}")

#alien_0={'x_position':0,'y_position':25, 'speed':'medium'}

#print(f"Original a_position:{alien_0['x_position']}")

#alien_0['speed']='fast'

#if alien_0['speed'] == 'slow':
	#increment=1
#elif alien_0['speed']=='medium':
	#increment=2
#else :
	#increment=3

#alien_0['x_position']=alien_0['x_position']+increment

#print(f"New x_positon: {alien_0['x_position']}")

#Removing a Key-Value Pairs
alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['color']
print(alien_0)

