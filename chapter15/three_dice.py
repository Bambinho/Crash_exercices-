from plotly.graph_objs import Bar, Layout 
from plotly import offline 

from die import Die 

die1=Die(6)
die2=Die(6)
die3=Die(6)

#Roll the dice
results=[]

for roll in range(1,10000):
	result=die1.roll()+die2.roll()+die3.roll()
	results.append(result)

##Calculating the frequency 
max_result=die1.num_sides+die2.num_sides+die3.num_sides
frequencies=[]
for value in range(3,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)

##Visualizing the data 

x_values=list(range(3,max_result+1))
data=[Bar(x=x_values,y=frequencies)]

xaxis_config={'title':'Rolling results','dtick':1}
yaxis_config={'title':'Frequencies'}
layout=Layout(title='Rolling three die of side 6',xaxis=xaxis_config,yaxis=yaxis_config)

offline.plot({'data':data,'layout':layout},filename='d6_3.html')


