import matplotlib.pyplot as plt 

x_values=range(1,1001)
y_values=[x**2 for x in x_values]
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)

###styling the plot 
ax.set_title("Scatter plot", fontsize=24)
ax.set_xlabel("Value",fontsize=12)
ax.set_ylabel("Squares of Value",fontsize=12)
ax.tick_params(axis='both',which='major',labelsize=14)
ax.axis([0,1100,0,1_100_000])
#plt.show()
plt.savefig('square_plot.png',bbox_inches='tight')
