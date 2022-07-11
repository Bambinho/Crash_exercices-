def make_album(a_name, alb_title,num_song=None):
	album={'artist_name':a_name,'album_title':alb_title}
	if num_song:
		album['number_of_song']=num_song
	return album

while True:
	print("\nPlease Enter The Album information?")
	print("(Enter 'q' to quit)")
	artist=input("\tArtist Name:")
	if artist=='q':
		break
	title=input("\tArtist Title:")
	if title=='q':
		break 
	music=make_album(artist,title)
	print(music)
















# music=make_album('Alpha Blondy','Newdawn')
# print(music)

# music=make_album('Micheal Jackson','Black and whyte ')
# print(music)

# music=make_album('Arafat','3500 volt')
# print(music)
# music=make_album('Alpha','Newdawn',10)
# print(music)