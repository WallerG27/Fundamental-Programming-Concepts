# Edit the code below

theSum = 0.0
count = 0
data = input("Enter a number or press Enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or press Enter to quit: ")
    count += 1
print("The sum is", theSum)
print("The average is", theSum / count)
