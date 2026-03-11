# Put your code here
#input
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

#math stuff
while smaller != 0:
    remainder = larger % smaller
    larger = smaller
    smaller = remainder


#output
print("The greatest common divisor is ", (larger))
