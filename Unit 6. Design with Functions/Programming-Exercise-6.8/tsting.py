# Put your code here
#This is a comment.
def printAll(seq):
    count = 0
    if seq:
        print(str(seq))
        count += 1
        print(count)
        printAll(seq[count:])
        if count == 2:
            print("tesint:", seq[1])



printAll([1, 2, 4, 5, 3, 6, 7, 5, 9, 8])
#Problem is you lose data and information, you can't cal old data
