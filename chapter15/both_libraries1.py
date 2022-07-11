import plotly.express as px
from refactoring import RandomWalk 
#Make a random walk 
#Keep making new random walk 

rw=RandomWalk(50000)
rw.fill_walk()

#fig,ax=plt.subplots(figsize=(10,6))
ax=px.scatter(rw.x_values,rw.y_values,labels={'x':'X values','y':'Y values'})
point_numbers=range(rw.num_points)


ax.show()



