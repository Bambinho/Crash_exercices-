import matplotlib.pyplot as plt 

from random_walk import RandomWalk 
#Make a random walk 
#Keep making new random walk 
while True:
	rw=RandomWalk()
	rw.fill_walk()
	plt.style.use('seaborn')
	fig,ax=plt.subplots()
	ax.scatter(rw.x_values,rw.y_values,c='red',s=5)
	ax.set_title("Visual of Random Walk")
	ax.set_xlabel("X values",fontsize=12)
	ax.set_ylabel("Y values",fontsize=12)
	ax.tick_params(axis='both',labelsize=15)
	plt.show()
	keep_running=input("Make another walk? (y/n): ")

	if keep_running==n:
		break

