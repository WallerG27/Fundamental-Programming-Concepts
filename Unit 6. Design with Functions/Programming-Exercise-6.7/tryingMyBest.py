# Put your code here
#this is a comment.
inFile = input("Enter the input file name: ")
outFile = input("Enter the output file name: ")

file = open(inFile, 'r')
text = file.read()

#OutputFile
outFile = open(outFile, "w")
outFile.write(text)
