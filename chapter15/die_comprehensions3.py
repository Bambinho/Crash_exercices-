from plotly.graph_objs import Bar, Layout 
from plotly import offline 

from die import Die 

#Simulating rolling a dice 
die1=Die()
die2=Die()
results=[die1.roll()*die2.roll() for roll in range(1,1000)]
##Calculating the frequency
max_result=die1.num_sides*die2.num_sides
frequencies=[results.count(value) for value in range(1,max_result+1)]
###Visualizing the data 
x_values=list(range(1,max_result+1))
data=[Bar(x=x_values,y=frequencies)]
xaxis_config={'title':'Value obtain after rolling two dice','dtick':1}
yaxis_config={'title':'Frequency Value'}
layout=Layout(title='Rolling two die of six sides and reporting the answer',xaxis=xaxis_config,
	yaxis=yaxis_config)

offline.plot({'data':data,'layout':layout},filename='multi.html')