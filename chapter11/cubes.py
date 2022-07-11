import matplotlib.pyplot as plt 

x_values=range(1,5001)
y_values=[x**3 for x in x_values]
plt.style.use("seaborn")

fig,ax= plt.subplots()

ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Oranges,s=10)

ax.set_title("Cube Graphs ")
ax.set_xlabel("Values",fontsize=12)
ax.set_ylabel("Cubes Values ", fontsize=12)

ax.tick_params(axis='both',labelsize=14)

plt.show()





