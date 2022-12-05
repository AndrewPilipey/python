import random
from math import sqrt

#lucky number
name = input("Your name is: ")

var_random = (random.randint(1, 10))

for i in range(4):
    print (" ::: ", name, " ::: , your lucky number is: ", var_random,)

print("Score your day's lucky: ", sqrt(25))
