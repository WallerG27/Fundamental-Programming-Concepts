"""
File: decrypt.py
Project 4.3

Decypts a file of encrypted text. and prints
the result.  The other input is the distance value.
"""
#input
enFile = input("Enter the input file name: ")
decFile = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))
code = ""

#InputFile
file = open(enFile, 'r')
text = file.readline()

#Converion
for ch in text:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    code +=  chr(cipherValue)

#OutputFile
decFile = open(decFile, "w")
decFile.write(code)
print(code)

#ask if this one wants it in two or one file
