# Put your code here
#input
salary = float(input("Enter the starting salary: "))
increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

#math stuff
increase = increase / 100
count = 1
startingSalary = salary

#output with math
print("Years    Salary")
print("--------------")
for eachPass in range(years):
    print("%2d%12.2f" % ((count), (startingSalary)))
    newPay = startingSalary * increase
    startingSalary = newPay + startingSalary
    count += 1
    #it's a format thing
