# What does this piece of code do?
# Answer:Randomly generate integers between 1 and 100 for 10 times and print the biggest one.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#initialize the variables
progress=0
stored_random_number=0
#create a loop which will run 10 times
while progress<10:
	progress+=1
#generate a random integer between 1 to 100
	n = randint(1,100)
#use the variable stored_random_number to store the biggest n
	if n > stored_random_number:
		stored_random_number = n
#print the biggest integer
print(stored_random_number)
