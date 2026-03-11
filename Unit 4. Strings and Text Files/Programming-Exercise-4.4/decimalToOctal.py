# Put your code here

decimal = int(input("Enter a string of octal digits:  "))
if decimal == 0: 
    print(0)
else:
    print("Quotient Remainder Octal")
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        octal = str(remainder) + octal
        print("%5d%8d%12s" % (decimal, remainder, octal))
    print("The octal representation is", octal)  
