# Put your code here
#input
import math
iter = int(input("Enter the number of iterations: "))

top = -1
bottom = 1
total = 0
count = 0
for eachPass in range(iter):
    top = -(top)
    total += (top / (bottom))
    print(total)
    bottom += 2  

#math stuff

#output
print("The approximation of pi is", (total*4))
