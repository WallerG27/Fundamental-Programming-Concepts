# Modify the code below:
import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
maxGuess = round(math.log(larger-smaller + 1, 2))

while True:
    count += 1
    print(smaller, larger)
    number = (smaller + larger) // 2
    print("Your number is", number)
    userInput = input("Enter =, <, or >: ")
    if userInput == "=":
        print("Hooray, I've got it in", (count), "tries")
        break

    elif count == maxGuess:
        print("I'm out of guesses, and you cheated")
        break

    elif userInput == ">":
        smaller = (number+1)
    
    else:
        larger = (number-1)
