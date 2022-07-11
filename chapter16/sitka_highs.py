import csv 
import matplotlib.pyplot as plt 
from datetime import datetime
filename='/home/timlinux/Downloads/crash_course/chapter16/data/sitka_weather_2018_simple.csv'

with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
	highs,dates,lows=[],[],[]
	for row in reader:
		high=int(row[5])
		low=int(row[6])
		date=datetime.strptime(row[2],'%Y-%m-%d')
		dates.append(date)
		highs.append(high)
		lows.append(low)


plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
ax.set_title(" Daily high and low temperatures -2018",fontsize=24)
ax.set_xlabel('Dates',fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Temperature in (T)',fontsize=12)
ax.tick_params(axis='both',which='major',labelsize=14)

plt.show()