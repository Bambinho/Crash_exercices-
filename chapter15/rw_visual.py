import matplotlib.pyplot as plt 

from refactoring import RandomWalk 
#Make a random walk 
#Keep making new random walk 
while True:
	rw=RandomWalk(50_000)
	rw.fill_walk()
	plt.style.use('seaborn')
	fig,ax=plt.subplots(figsize=(10,6))
	point_numbers=range(rw.num_points)
	ax.scatter(rw.x_values,rw.y_values,c=point_numbers,edgecolors='none',cmap=plt.cm.Blues,s=1)
	ax.set_title("Visual of Random Walk")
	ax.set_xlabel("X values",fontsize=12)
	ax.set_ylabel("Y values",fontsize=12)
	ax.tick_params(axis='both',labelsize=15)

	###Plotting the end and begining of the datapoint
	ax.scatter(0,0,c='green',edgecolors='none',s=100)
	ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

	###Remove the axes.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	plt.show()
	keep_running=input("Make another walk? (y/n): ")
	if keep_running=='n':
		break

