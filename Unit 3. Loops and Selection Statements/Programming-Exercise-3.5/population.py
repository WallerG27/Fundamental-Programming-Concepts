# Put your code here
numOrg = int(input("Enter the initial number of organisms: "))
growth = float(input("Enter the rate of growth [a real number > 1]: "))
hourRate = int(input("Enter the number of hours to achieve the rate of growth: "))
hourTake = int(input("Enter the total hours of growth: "))

#math stuff

loop = hourTake // hourRate
for eachPass in range(loop):
    numOrg = numOrg * growth

#output
print("The total population is", int(numOrg))
