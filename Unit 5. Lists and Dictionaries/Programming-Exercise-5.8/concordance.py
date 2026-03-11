# Put your code here
#This is a comment.

#input
fileName = input("Enter the input file name: ")

inputFile = open(fileName, 'r')
text = inputFile.read()




#finds each word and counts it
def wordCount(str):
    counts = dict()
    words = str.split()
    
    
    for word in words:
        if word in counts:
            counts[word] += 1
            
        else:
            counts[word] = 1
            
  
    
    return counts
    






#output stuff
print('')
wordList = list(wordCount(text))

sortedWords = (sorted(list(set(wordList))))

totalWords = len(wordCount(text))

whichWord = 0

table = wordCount(text)

while totalWords > whichWord:
    print((sortedWords[whichWord]), table[sortedWords[whichWord]])
    whichWord += 1
