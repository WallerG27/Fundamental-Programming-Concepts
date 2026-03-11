# Put your code here
#input
message = str(input("Enter a message: "))
distance = int(input("Enter the distance value: "))
code = ""

#math
for ch in message:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    code += chr(cipherValue)
print(code)


