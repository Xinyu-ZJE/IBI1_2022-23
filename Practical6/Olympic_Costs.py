#creat a sorted list
my_list=[]
cost=[1,8,15,7,5,14,43,40]
sorted_cost=sorted(cost)
print(sorted_cost)

#Firstly, create a sorted dictionary
#Secondly, import the dictionary into the bar plot
my_dict={}
costs = {'Los Angeles 1984': 1, 'Seoul 1988': 8, 'Barcelona 1992': 15, 'Atlanta 1996': 7, 'Sydney 2000': 5, 'Athens 2003': 14, 'Beijing 2008': 43, 'London 2012': 40}
# 'items()' convert the dictionary into tuple, which is two related array in this case.
# "key=..." means sort the arrays according to the size of number in ... 
# lambda function extracts the values corresponding to keys.
sorted_costs=sorted(costs.items(),key=lambda x:x[1])
# convert the tuple into dictionary
my_dict=dict(sorted_costs)

import numpy as np
import matplotlib.pyplot as  plt
#import the number of groups on the X-axis
ind=np.arange(len(my_dict.keys()))
# The width of the bars
width=0.5
# The colors of bars
colors='red','yellow','blue'
#The lengh/height ratio
plt.figure(figsize=(10,5))
#the title of the bar chart
plt.title ('The relationship between costs of hosting the Summer Olympic Games and years')
#rotate the xlabels,change the sizes of labels
plt.xticks(rotation=30,fontsize=8)
plt.xticks(ind,my_dict.keys())
plt.ylabel('Cost(in $ billions)')
#np.arange:[start,stop,step]
plt.yticks(np.arange(0,41,5))
plt.bar(ind,my_dict.values(),width,color=colors)
plt.show()
