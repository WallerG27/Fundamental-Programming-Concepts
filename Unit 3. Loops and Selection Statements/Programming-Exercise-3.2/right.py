#input
first = int(input("Enter the first side: "))
second = int(input("Enter the second side: "))
third  = int(input("Enter the third side: "))

#math stuff
firstS = first**2
secondS = second**2
thirdS = third**2

#output
if firstS + secondS == thirdS:
    print("The triangle is a right triangle.")
elif thirdS + secondS == firstS:
    print("The triangle is a right triangle.")
elif thirdS + firstS == secondS:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")

