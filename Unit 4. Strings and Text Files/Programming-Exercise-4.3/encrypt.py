"""
File: encrypt.py
Project 4.3

Encypts a text file.  The inputs are the names of
the input file and the output file and the distance value.
The encrypted code is witten to a new file.
"""
#input
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

#OutputFile
text = open(inName, 'r')
file = text.read()

#Converion
code = ""
outFile = open(outName, 'w')
for ch in file:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code += chr(cipherValue)

#InputFile
outFile.write(code)
outFile.close()


