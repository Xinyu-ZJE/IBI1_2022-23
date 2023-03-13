a=-3.19
b=-118.24
c=116.39
d=a-b
e=c-a
if d>e:
 print ("Los Angeles")
else:
 print ("Haining")

#actually, the flowing method is more rigorous:
if d>e:
 print ("Los Angeles")
elif d<e:
 print ("Haining")
else:
 print ("The distances are the same")

#The output is "Haining", so the trip to Haining is further than the trip to Los Angeles.

X=True
Y=False
W=X and Y
Z=X or Y
print (W)
print (Z)

