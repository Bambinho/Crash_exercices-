import csv 
from datetime import datetime
import matplotlib.pyplot as plt 

filename='/home/timlinux/Downloads/crash_course/chapter16/data/death_valley_2018_simple.csv'

with open(filename) as f :
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
	for index, column_name in enumerate(header_row):
		print(index,column_name)
	dates,falls=[],[]

	for row in reader :
		date=datetime.strptime(row[2],'%Y-%m-%d')
		try:
			fall=float(row[3])
		except ValueError:
			print(f"Value missing for {date}")
		else :
			dates.append(date)
			falls.append(fall)

plt.style.use('seaborn')

fig,ax= plt.subplots()

ax.plot(dates,falls,c='blue')
plt.title("Amount of Rainfall in Sitka in-2018",fontsize=20)
plt.xlabel('',fontsize=12)
plt.ylabel('Rainfall',fontsize=12)
fig.autofmt_xdate()
plt.savefig('death_valley.png')
plt.show()


