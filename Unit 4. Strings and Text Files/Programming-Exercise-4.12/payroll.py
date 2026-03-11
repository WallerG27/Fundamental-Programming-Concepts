# Put your code here
#This is a comment
#input
fileName = input("Enter the file name: ")
names = []
hours = []
tPay = []

#open the file and read
with open(fileName, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.split() 
        names.append(line[0]) 
        hours.append(int(line[1]))
        tPay.append(float(line[2]))

#ouput        
print(f'{"Name":14s}{"Hours":9s}{"Total Pay":13s}')
for name, hour, pay in zip(names, hours, tPay):
    
    pay = float(pay)
    hour = int(hour)
    pay = pay * hour
    
    print(f"{name:15s}{hour}{pay:13.2f}")


