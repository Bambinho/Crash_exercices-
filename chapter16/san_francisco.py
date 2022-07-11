import csv 

from datetime import datetime 
import matplotlib.pyplot as plt 

filename='/home/timlinux/Downloads/crash_course/chapter16/data/san_francisco_2022_full.csv'

with open(filename) as f :
	reader=csv.reader(f)
	header=next(reader)

	print(header)

	highs,lows,dates=[],[],[]
	for row in reader:
		date=datetime.strptime(row[5],'%Y-%m-%d')
		try:
			low=int(row[22])
			high=int(row[20])
		except:
			pass
		else:
			if date in dates:
				pass
			else:
				highs.append(high)
				lows.append(low)
				dates.append(date)

plt.style.use('seaborn')

fig,ax=plt.subplots()
ax.plot(dates,lows,c='red',alpha=0.5)
ax.plot(dates,highs,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,alpha=0.1)

plt.ylim(0,120)
plt.savefig('san_francisco.png')
plt.show()
