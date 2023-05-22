# make a dictionary
my_dict={}
movie={'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fictioin':22,'Horror':19,'Crime':18,'Documetary':12,'History':8,'War':7}

#realize the interaction with users
chosen=input('the movie genre:(capitalize the first letter)')
print(movie.get(chosen,'notfound'))

import matplotlib.pyplot as plt
#import the dictionary in to the pie chart
labels=movie.keys()
sizes=movie.values()
#the numbers of explode represent the distance of the sector from the center of the circle
explode=(0,0,0,0,0,0,0,0,0,0.3)
#autopct is the significant figures
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%")
plt.title ('Favourite movie genres among Chinese university students')
plt.show()
