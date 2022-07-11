import csv 
from datetime import datetime
import  matplotlib.pyplot as plt

# filename='/home/timlinux/Downloads/crash_course/chapter16/data/san_francisco_2022_full.csv'

filename='/home/timlinux/Downloads/crash_course/chapter16/data/death_valley_2018_simple.csv'

#filename='/home/timlinux/Downloads/crash_course/chapter16/data/sitka_weather_2018_simple.csv'

with open(filename) as f :

	reader=csv.reader(f)
	header_row=next(reader)
	for index, value in enumerate(header_row):

		if value=='TMIN':
			MIN=index
		if value=='TMAX':
			MAX=index
		if value=='NAME':
			NAME=index
		if value=='DATE':
			DATE=index
	dates,highs,lows=[],[],[]

	for row in reader:
		date=datetime.strptime(row[DATE],'%Y-%m-%d')
		station=row[NAME]
		try:
			low=int(row[MIN])
			high=int(row[MAX])
		except ValueError :
			pass
		else:
			if date in dates:
				pass
			else:
				lows.append(low)
				highs.append(high)
				dates.append(date)

plt.style.use('seaborn')

fig,ax= plt.subplots()

ax.plot(dates,highs,color='red',alpha=0.6)
ax.plot(dates,lows,color='blue',alpha=0.6)
ax.fill_between(dates,highs,lows,color='blue',alpha=0.1)

plt.title(f" High and Low temperature for {station} ")

plt.show()





