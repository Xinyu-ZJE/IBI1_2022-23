#repeat
#	count the generations of rabbits
#	how many rabbits are there already?
#		If the total number is smaller than 100:keep counting
#		If larger than 100: print the generation number

num=2 #the initial number is 2
gen=1 #the initial generation is 1
while num<100:
 gen=gen+1
#pow (a,b) means a^b
 num=pow (2,gen)
gen=str(gen)
print ("At the",gen,"th generation, over 100 rabits have been born.")

#The output is "At the 7 th generation, over 100 rabits have been born."
