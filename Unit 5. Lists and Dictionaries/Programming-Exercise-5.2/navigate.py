# Put your code below:
#This is a comment.

#user input
file = input("Enter the input file name: ")

#opens and reads the file
openLines = open(file, "r")
tLines = sum(1 for _ in open(file))
lines = openLines.readlines()

#so the loop doesn't blow up
LineNum = ''

#loop
while (LineNum != 0):
    
    #input
    print("The file has", (tLines), "lines.")
    LineNum = int(input("Enter a line number [0 to quit]: "))
    
    #Error
    if LineNum > tLines:
        print("ERROR: line number must be less than", (LineNum - 1), ".")

    #Working
    elif LineNum > 0:
        print(LineNum, ":", (lines[LineNum - 1]))
