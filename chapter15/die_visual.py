from plotly.graph_objs import Bar, Layout
from plotly import offline 


from die import Die 

die=Die()

results=[]
for roll_num in range(1000):
	results.append(die.roll())

##Analyze the results.
frequencies=[]
for value in range(1,die.num_sides+1):
	frequencie=results.count(value)
	frequencies.append(frequencie)
#Visualize the results 
x_values=list(range(1,die.num_sides+1))
data=[Bar(x=x_values,y=frequencies)]


x_axis_config={'title':'results'}
y_axis_config={'title':'Frequencies of Result'}
my_layout=Layout(title='Results of rolling one D6 1000 times',
	xaxis=x_axis_config,yaxis=y_axis_config)

offline.plot({'data':data,'layout':my_layout},filename='d6.html')










#print(results )
print("\n")
print(frequencies)