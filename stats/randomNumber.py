# Nate-ar
# sep 5 23
# for stats class random sample selection from range
import random
# get the min and max of the range
min = input("Min> ")
max = input("Max> ")
# init the population array with the min number first
pop = [int(min)]
# run a for loop where x is a number in the rand min-max
for x in range(int(min),int(max)):
    # add each number in between to the array
    pop.append(int(min)+x)
# print get the number of samples they want and use random.samlple
print(random.sample(pop,int(input("K= >"))))