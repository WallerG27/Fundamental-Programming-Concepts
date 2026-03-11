# Put your code here
#This is a comment.

###Defing junk
#Mean
def mean(list):
    lenList = len(list)
    i = 0
    sum = 0

    while i < lenList:
        sum += list[i]
        i += 1
    return sum/lenList

#Median
def median(list):
    lenList = len(list)
    list = sorted(list)
    mid = lenList // 2

    if lenList % 2 == 0:
        return (list[mid]+list[mid - 1]) / 2
    else:
        return list[mid]

#Mode
def mode(lyst):
    saveDict = dict()
    mode = False
    modeValue = 0
    result = 0

    for x in lyst:
        if(not saveDict.get(x)):
            saveDict[x] = 1
        else:
            saveDict[x] += 1
            mode = True
  
        if(saveDict[x] > modeValue):
            modeValue = saveDict[x]
            result = x

    if(mode):
        return result
    else:
        return "No mode"



#Main
def main():
    lyst = [3, 1, 7, 1, 4, 10]
    print("List:",(lyst))
    print("Mode:",mode(lyst))
    print("Median:",median(lyst))
    print("Mean:",mean(lyst))

#Code starts here
main()
