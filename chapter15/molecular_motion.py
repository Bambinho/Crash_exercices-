import matplotlib.pyplot as plt 
from modified_random_walk import RandomWalk 

rw=RandomWalk()
rw.fill_walk()
plt.style.use('seaborn')

fig,ax=plt.subplots()

ax.plot(rw.x_values,rw.y_values,c='blue',linewidth=0.5)
ax.scatter(0,0,c='green',s=200)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=200)
ax.set_xlabel("X values",fontsize=12)
ax.set_ylabel("Y values",fontsize=12)
ax.set_title("Random walk",fontsize=25)

plt.show()