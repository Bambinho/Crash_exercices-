from plotly.graph_objs import Bar, Layout 
from plotly import offline
from die import Die 

die1=Die()
die2=Die(10)
results =[]

for num_roll in range(1,50_000):
	result=die1.roll()+die2.roll()
	results.append(result)
frequencies=[]

num_max=die1.num_sides + die2.num_sides

for value in range(2,num_max+1):
	frequency=results.count(value)
	frequencies.append(frequency)

x_values=list(range(2,num_max+1))
data=[Bar(x=x_values,y=frequencies)]

axis_xlayout={'title':' X values','dtick':1}
axis_ylayout={'title':'Y values'}
layout=Layout( title='Result of rolling and D6 and D10 die ',xaxis=axis_xlayout,yaxis=axis_ylayout)

offline.plot({'data':data,'layout':layout},filename='d6_d10.html')