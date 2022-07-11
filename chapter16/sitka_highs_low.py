import csv
from datetime import datetime 
import matplotlib.pyplot as plt  

def read_func(filename,highs,lows,dates,x,y):
	with open(filename) as f :
		reader=csv.reader(f)
		header=next(reader)
		print(header)
		#highs,lows,dates=[],[],[]
		for row in reader:
			date=datetime.strptime(row[2],'%Y-%m-%d')
			try:
				high=int(row[x])
				low=int(row[y])
			except ValueError:
				print(f"Missing data for {date}")
			else:
				dates.append(date)
				highs.append(high)
				lows.append(low)



filename='/home/timlinux/Downloads/crash_course/chapter16/data/sitka_weather_2018_simple.csv'
highs,lows,dates=[],[],[]
read_func(filename,highs,lows,dates,5,6)

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)
plt.title("Low and high temperature for the year-2018 ",fontsize=14)
plt.xlabel('',fontsize=12)
plt.ylabel('Temperature',fontsize=12)
plt.ylim(0,140)
fig.autofmt_xdate()

filename='/home/timlinux/Downloads/crash_course/chapter16/data/death_valley_2018_simple.csv'
highs,lows,dates=[],[],[]
read_func(filename,highs,lows,dates,4,5)



ax.plot(dates,highs,c='red',alpha=0.8)
ax.plot(dates,lows,c='blue',alpha=0.8)
ax.fill_between(dates,lows,highs,facecolor='blue',alpha=0.3)


plt.show()



