import matplotlib.pyplot as plt 

from die import Die 

plt.style.use('_mpl-gallery')

die=Die()
results =[die.roll() for roll in range(1,100)]
max_value=die.num_sides
frequencies=[results.count(value) for value in range(1,max_value+1)]

fig,ax= plt.subplots()
x_values=list(range(1,max_value+1))
ax.bar(x_values,frequencies, width=1, edgecolor="white", linewidth=0.7)

ax.set_title("Visual of Random Walk")
ax.set_xlabel("X values",fontsize=12)
ax.set_ylabel("Y values",fontsize=12)
ax.tick_params(axis='both',labelsize=15)

#ax.set(xlim=(0, 8), xticks=list(range(1, 8)), ylim=(0, 8), yticks=list(range(1, 8)))
plt.show()


