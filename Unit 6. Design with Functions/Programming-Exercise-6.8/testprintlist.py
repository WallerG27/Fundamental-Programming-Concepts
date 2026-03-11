# Put your code here
#This is a comment.
def printAll(seq):
    if seq:
        print(str(seq))
        print(seq[0])
        printAll(seq[1:])


printAll([1, 2, 4, 5, 3, 6, 7, 5, 9, 8])
#Problem is you lose data and information, you can't cal old data
