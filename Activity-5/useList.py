# This program exercises lists.

# The following files must be in the same folder:
#   abstractcollection.py
#   abstractlist.py
#   arraylist.py
#   arrays.py
#   linkedlist.py
#   node.py
#   input.txt - the input text file.

# Input: input.txt
#   This file must be in the same folder.
#   To keep things simple:
#     This file contains no punctuation.
#     This file contains only lowercase characters. 
# Output: output.txt
#   This file will be created in the same folder.
#   All articles are removed.
#   Certain prepositions are removed.
#   Duplicate consecutive words are reduced to a single occurrence.
#     Note: The words "first" and "last" are not reduced.
#   Certain misspelled words are flagged.
#   Occurrences of "first" are moved to the front of a line.
#   Occurrences of "last" are moved to the end of a line.

from arraylist import ArrayList
from linkedlist import LinkedList

# Data:

articles = ArrayList(["a", "the"])
prepositions = LinkedList(["after", "before", "from", "in", "off", "on", "under", "out", "over", "to"])
misspellings = ["foriegn", "excede", "judgement", "occurrance", "preceed", "rythm", "thier", ]

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

FIRST = "first"
FLAG = "FLAG:"
LAST = "last"

# Processing:

# Part 1:
# Removes all items from the words list that are found in the removals list.
# Input:
#   words - an ArrayList of words, no uppercase, no punctuation
#   wordsIter - a list iterator for the words list
#   removals - the list of words to remove
def removeItems(words, wordsIter, removals):
    # <your code>
    wordsIter.first()
    while (wordsIter.hasNext()):
        word = wordsIter.next()
        if (word in removals):
            wordsIter.remove()

# Part 2:
# Removes extra occurrances of consecutive duplicate words from the words list.
#   Note: It does not reduce the words "first" and "last".
# Input:
#   words - an ArrayList of words, no uppercase, no punctuation
#   wordsIter - a list iterator for the words list
def reduceDuplicates(words, wordsIter):
    # <your code>
    previousWord = ''
    wordsIter.first()
    while (wordsIter.hasNext()):
        word = wordsIter.next()
        if (word == FIRST) or (word == LAST):
            previousWord = word
            continue
        if (word == previousWord):
            wordsIter.remove()
            previousWord = word

# Part 3:
# Flags certain misspelled words in the words list by inserting "FLAG:" before them.
# Input:
#   words - an ArrayList of words, no uppercase, no punctuation
#   wordsIter - a list iterator for the words list
#   misspellings - the list of misspelled words to flag
def flagMisspelled(words, wordsIter, misspellings):
    # <your code>
    while (wordsIter.hasNext()):
        word = wordsIter.next()
        if (word in misspellings):
            wordsIter.insert(FLAG)
            wordsIter.next()

# Part 4:
# Move all occurrences of "first" to the front of the words list.
# Input:
#   words - an ArrayList of words, no uppercase, no punctuation
#   wordsIter - a list iterator for the words list
def moveFirstLit(words, wordsIter):
    # <your code>
    countFirst = 0
    wordsIter.first()
    while (wordsIter.hasNext()):
        word = wordsIter.next()
        if (word == FIRST):
            wordsIter.remove()
            countFirst += 1
    for count in range(countFirst):
        wordsIter.first()
        if (wordsIter.hasNext()):
            wordsIter.next()
        wordsIter.insert(FIRST)

# Part 5:
# Move all occurrences of "last" to the end of the words list.
# Input:
#   words - an ArrayList of words, no uppercase, no punctuation
#   wordsIter - a list iterator for the words list
def moveLastLit(words, wordsIter):
    # <your code>
    countLast = 0
    wordsIter.last()
    while (wordsIter.hasNext()):
        word = wordsIter.next()
        if (word == LAST):
            wordsIter.remove()
            countLast += 1
    for count in range(countLast):
        wordsIter.last()
        if (wordsIter.hasNext()):
            wordsIter.next()
        wordsIter.insert(LAST)


def writeOutputLine(words):
    outputLine = " ".join(words)
    outputLine = outputLine + "\n"
    print(outputLine, end="")
    outputFile.write(outputLine)

# Main processing loop:
for line in inputFile:
    words = ArrayList(line.split())
    wordsIter = words.listIterator()

    # Make no changes to blank lines:
    if (len(words) == 0):
        writeOutputLine(words)
        continue

    # Make no changes to comment lines:
    if (words[0] == "#"):
        writeOutputLine(words)
        continue

    # Remove articles:
    removeItems(words, wordsIter, articles)
    
    # Remove prepositions:
    removeItems(words, wordsIter, prepositions)

    # Reduce duplicate consecutive words to a single occurrence:
    reduceDuplicates(words, wordsIter)

    # Insert "FLAG:" before certain misspelled words:
    flagMisspelled(words, wordsIter, misspellings)
    
    # Move all occurrences of "first" to the front of the line:
    moveFirstLit(words, wordsIter)
        
    # Move all occurrences of "last" to the end of the line:
    moveLastLit(words, wordsIter)

    # Write output line:
    writeOutputLine(words)

# Wrap-up
inputFile.close()
outputFile.close()

