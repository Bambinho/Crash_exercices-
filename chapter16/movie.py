import csv 
filename='/home/timlinux/Downloads/crash_course/chapter16/data/small.csv'

with open(filename) as f :
	reader=csv.reader(f)
	header=next(reader)

	print(header)

	# for row in reader:
	# 	print(row)