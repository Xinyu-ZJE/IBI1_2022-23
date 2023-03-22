# make a dictionary
my_dict={}
movie={'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fictioin':22,'Horror':19,'Crime':18,'Documetary':12,'History':8,'War':7}

#two methods to  realize the interaction with users
# the first one: chosen
chosen=input('the movie genre:(capitalize the first letter)')
a=movie.get(chosen,'notfound')
print(a)
# the second one: if loop
key=input('the movie genre:(capitalize the first letter)')
if key in movie.keys():
    print(movie[key])
else:
    print('notfound')
#draw pie chat in two methods
#the first one, do not depent on the dictionary
import numpy as np
import matplotlib.pyplot as plt
# the label is counter-clockwise
labels ='Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Dpcumentary','History','War'
sizes= [73,42,38,28,22,19,18,12,8,7]
#the numbers of explode represent the distance of the sector from the center of the circle
explode=(0,0,0,0,0,0,0,0,0,0.3)
#autopct is the significant figures
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%")
#ensure that the pie is drawn as a circle
plt.axis('equal')
plt.title ('Favourite movie genres among Chinese university students(Method1)')
plt.show()

#The second one is to import the dictionary into the pie chart
import numpy as np
import matplotlib.pyplot as plt
labels=movie.keys()
sizes=movie.values()
explode=(0,0,0,0,0,0,0,0,0,0.3)
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%")
plt.title ('Favourite movie genres among Chinese university students(Method2)')
plt.show()
