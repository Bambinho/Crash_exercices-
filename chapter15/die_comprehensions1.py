from plotly.graph_objs import Bar, Layout 
from plotly import offline
from die import Die 

die1=Die(8)
die2=Die(8)

results=[ die1.roll()+die1.roll() for roll in range(1,1000)]

result_max=die1.num_sides+die1.num_sides 
frequencies=[results.count(value) for value in range(2,result_max+1)]


x_values=list(range(2,result_max+1))

data=[Bar(x=x_values,y=frequencies)]

xaxis_config={'title':'D8 result value','dtick':1}
yaxis_config={'title':'Frequency'}

layout=Layout(title='Rolling tow d8 dice',xaxis=xaxis_config,yaxis=yaxis_config)

offline.plot({'data':data,'layout':layout},filename='d8.html')


