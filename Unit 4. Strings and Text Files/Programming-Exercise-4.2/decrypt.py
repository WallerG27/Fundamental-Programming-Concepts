# Put your code here
#input
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
message = ""

#math
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    message += chr(cipherValue)
print(message)
