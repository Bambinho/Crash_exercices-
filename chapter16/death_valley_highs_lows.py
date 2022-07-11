import csv 
from datetime import datetime
import matplotlib.pyplot as plt 

filename='/home/timlinux/Downloads/crash_course/chapter16/data/death_valley_2018_simple.csv'

with open(filename) as f:

	reader=csv.reader(f)
	header=next(reader)
	# for index, value in enumerate(header):
	# 	print(index,value)

	highs,lows,dates=[],[],[]

	for row in reader:
		date=datetime.strptime(row[2],'%Y-%m-%d')
		try:
			high=int(row[4])
			low=int(row[5])
		except ValueError:
			print(f"Missing data for {date}")
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)

plt.style.use('seaborn')
#
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,alpha=0.1)

plt.title("Daily Lows and Highs Temperature-2018 in\n death Valley,CA",fontsize=15)
plt.xlabel('Date',fontsize=12)
plt.ylabel('Temperature',fontsize=12)

fig.autofmt_xdate()

plt.show()









