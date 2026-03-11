# Put your code here
#this is a comment.
import os

inName = input("Input filename: ") 
outName = input("Output filename: ") 
inputFile = open(inName, "r") 
outputFile = open(outName, "w") 
count = 1 
for line in inputFile: 
  newLine = str(count).rjust(4, " ") + "> " + line 
  outputFile.write(newLine) 
  print(newLine) 
  count += 1




#inputs
#fileUno = input("Enter the input file name: ")
#fileDos = input("Enter the ouput file name: ")
#number = 1

#test files
#inExist = os.path.exists(fileUno)
#outExist = os.path.exists(fileDos)

#created file if it doesn't exist
#if inExist == False:
    #inTest = open(fileUno, 'w')
#outTest = open(fileDos, 'w')

#opens one as a file and reads it
#fileOne = open(fileUno, 'r')
#text = fileOne.readline()

#OutputFile
#outFile = open(fileDos, "w")
#print(number), ">", (text)

#nText = ((number), ">", (text))

#outFile.write(nText)
#number +=1
