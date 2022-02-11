# This is a simple algorithm which creates a list of random integers
# from 0 to 9, of a random length from 4 to 10
# it then asks user to guess all numbers and once all numbers are guessed the script ends

import random

m = random.randint(4,10)
a = []
for i in range(m):
    n = random.randint(0, 9)
    a.append(n)

while True:
    answer = input("Enter number or X to exit")
    if answer == 'X':
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Invalid entry. Please enter X for exit or number to guess")
    if answer in a:
        print("You guessed!")
        a.pop(a.index(answer))
        print("There are {} more numbers to guess".format(len(a)))
        if len(a)==0:
            break
    else:
        print("Incorrect!")


