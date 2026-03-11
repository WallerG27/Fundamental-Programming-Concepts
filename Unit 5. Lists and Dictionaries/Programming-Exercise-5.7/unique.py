# Put your code here
#This is a comment.
#sorting the words
def sortWords(fileName):
    fileOpen = open(fileName,'r')
    fileRead = fileOpen.read()
    fileOpen.close()
    newWord = []
 
    wordList = fileRead.split()

    for word in wordList:
        if word not in newWord:
            newWord.append(word)
           
    print("\n".join(sorted(list(set(newWord)))))


#input
def main():
    fileName = input("Enter the input file name: ")
    sortWords(fileName)

main()







