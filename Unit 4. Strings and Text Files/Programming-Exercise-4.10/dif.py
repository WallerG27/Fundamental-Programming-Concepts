"""
File: dif.py
Project 4.10

Deterines whether or not the contents of two text
files are the same.  Outputs "Yes" if that is the
case or "No" and the first two lines that differ if
that is not the case.
"""
# Put your code here
#this is a comment.
inFile = input("Enter the input file name: ")
outFile = input("Enter the output file name: ")

inFileRead = open(inFile, 'r')
outFileRead = open(outFile, 'r')

inFileLines = inFileRead.readlines()
inFileRead.close()
outFileLines = outFileRead.readlines()
outFileRead.close()

lineCount = 0

while lineCount != len(inFileLines):

    if inFileLines[lineCount] == outFileLines[lineCount]:
        lineCount += 1
        if lineCount == len(inFileLines):
            print("Yes")
    elif inFileLines[lineCount] != outFileLines[lineCount]:
        print("No")
        print(inFileLines[lineCount])
        print(outFileLines[lineCount])
        break






#import os

#checks if it exist to not overwrite
#inExist = os.path.exists(inFile)
#outExist = os.path.exists(outFile)

#created file if it doesn't exist
#if inExist == False:
    #inTest = open(inFile, 'w')
#if outExist == False:
    #outTest = open(outFile, 'w')

#open file as a text
#inTest = open(inFile, 'r')
#outTest = open(outFile, 'r')

#save the text as a verable
#inFinal = inTest.read()
#outFinal = outTest.read()

#OutputFile
#if inFinal == outFinal: 
    #print("Yes")
#else:
    #print("No")
