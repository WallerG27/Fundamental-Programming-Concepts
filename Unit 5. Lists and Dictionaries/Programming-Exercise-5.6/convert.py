# Put your code here
#This is a comment.
#some kind of table thing
repTable = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
    '5': 5, '6': 6,  '7': 7,  '8': 8,  '9': 9,  
    'A': 10,  'B': 11,  'C': 12,  'D': 13,  
    'E': 14,  'F': 15}

#Decimal to Rep
def decimalToRep(decimal, base):
    if decimal == 0: 
        print(0)
    else:
        bstring = ""
        remainder = decimal % base
        while decimal > 0:
            if remainder < 10:
                remainder = decimal % base
                decimal = decimal // base
                bstring = str(remainder) + bstring
            else:
                bstring += chr(65+(remainder%10))
                decimal = decimal // base
                bstring = bstring[::-1]
        return bstring

# A main for testing your program
def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))

# The entry point for program execution
if __name__ == "__main__":
    main()
