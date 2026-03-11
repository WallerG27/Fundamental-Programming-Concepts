"""
Program: textanalysis.py
Author: Ken
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)


    if word.count('aa'):
        syllables -= 1
    if word.count('ae'):
        syllables -= 1
    if word.count('ai'):
        syllables -= 1
    if word.count('ao'):
        syllables -= 1
    if word.count('au'):
        syllables -= 1

    if word.count('ea'):
        syllables -= 1
    if word.count('ee'):
        syllables -= 1
    if word.count('ei'):
        syllables -= 1
    if word.count('eo'):
        syllables -= 1
    if word.count('eu'):
        syllables -= 1

    if word.count('ia'):
        syllables -= 1
    if word.count('ie'):
        syllables -= 1
    if word.count('ii'):
        syllables -= 1
    if word.count('io'):
        syllables -= 1
    if word.count('iu'):
        syllables -= 1

    if word.count('oa'):
        syllables -= 1
    if word.count('oe'):
        syllables -= 1
    if word.count('oi'):
        syllables -= 1
    if word.count('oo'):
        syllables -= 1
    if word.count('ou'):
        syllables -= 1

    if word.count('ua'):
        syllables -= 1
    if word.count('ue'):
        syllables -= 1
    if word.count('ui'):
        syllables -= 1
    if word.count('uo'):
        syllables -= 1
    if word.count('uu'):
        syllables -= 1



    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables") 
