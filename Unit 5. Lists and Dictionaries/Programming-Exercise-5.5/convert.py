# Put your code here
#This is a comment.
#some kind of table thing
repTable = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
    '5': 5, '6': 6,  '7': 7,  '8': 8,  '9': 9,  
    'A': 10,  'B': 11,  'C': 12,  'D': 13,  
    'E': 14,  'F': 15}

#Binary to Decimal
def repToDecimal(rep, base):
    decimal = 0
    exponent = len(rep) - 1
    for digit in rep:
        decimal += repTable[digit] * base ** exponent
        exponent -= 1
    return decimal



# A main for testing your program
def main():
    """Tests the function."""
    print(repToDecimal('10', 10))
    print(repToDecimal('10', 8))
    print(repToDecimal('10', 2))
    print(repToDecimal('10', 16))

# The entry point for program execution
if __name__ == "__main__":
    main()
