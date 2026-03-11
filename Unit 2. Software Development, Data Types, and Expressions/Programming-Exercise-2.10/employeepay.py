# Put your code here
#Input
wage =  float(input("Enter the wage: $"))
regHour = float(input("Enter the regular hours: "))
overHour = float(input("Enter the overtime hours: "))

#math stuff
regPay = (wage)*(regHour)
overPay = ((wage)*1.5)*(overHour)
totalPay = (regPay)+(overPay)

#output
print("The total weekly pay is $", (totalPay))
