# from plotly.graph_objs import Bar, Layout 

# from plotly import offline 

import matplotlib.pyplot  as plt 

from die import Die 


die1=Die()
die2=Die()

results=[die1.roll()+die2.roll() for roll in range(1,1000)]

max_result= die1.num_sides +die2.num_sides 

frequencies=[results.count(value) for value in range(2,max_result)]


plt.style.use('seaborn')

fig,ax=plt.subplots()
x_values=range(2,max_result)
ax.bar(x_values,frequencies,edgecolor="white",width=1,linewidth=0.7)
plt.xlabel('title')
ax.tick_params(axis='both',which='major',labelsize=12)

plt.show()







# x_values=list(range(2,max_result))

# data=[Bar(x=x_values,y=frequencies)]
# xaxis_conf={'title':'rolling value','dtick':1}
# yaxis_conf={'title':'frequencies of rolling values'}
# layout=Layout(title='Bar Chart for rolling two dices',xaxis=xaxis_conf,yaxis=yaxis_conf)

# offline.plot({'data':data,'layout':layout},filename='test_d6.html')

