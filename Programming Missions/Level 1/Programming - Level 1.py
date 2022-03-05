from ctypes import sizeof
import os
import sys
import time

wordlistArray = []
nameArray = []

printS = False

# Reads wordlist and file with names and adds them to two arrays
def addToArray(wordlist):
    name = str(wordlist + "Array")
    with open(wordlist, 'r') as f:
        for line in f.readlines():
            #print("{}".format(line.strip()))
            if wordlist == 'wordlist.txt':
                wordlistArray.append(line.strip())
            else:
                nameArray.append(line.strip())
        if wordlist == 'wordlist.txt' and printS == True:
            print(wordlistArray)
        elif printS == True:
            print(nameArray)

addToArray('wordlist.txt')
addToArray('names.txt')


# Loops over the names array and for every name it loops over the wordlist array and counts number of characters and checks if the match.
# Also does other checks and when a word from the dictionary matches a word in the names array it adds it to a results.txt file.
# Otherwise it continues on to the next word
for name in nameArray:
    for word in wordlistArray:
        for n in range(len(name)):
            for w in range(len(word)):
                #print("-----")
                #print("{}{}{}".format(word[w] in name, n+1, len(name)))
                #print("Wordlist: \t{}\nName: \t\t{}\nWorlist w: \t{}\nName n: \t{}".format(word, name, word[w], name[n]))
                
                if word.count(name[n]) == name.count(name[n]):
                    if name[n] in word and len(word) == len(name):
                        if n+1 == len(name) and w+1 == len(word):
                        
                            print('Found')
                            with open('results.txt', 'a') as f:
                                f.write(word)
                                f.write(", ")
                            nextWord = True
                            nextWord = True
                            break
                else:
                    print('next word')
                    nextWord = True
                    break
            if nextWord == True:
                nextWord = False
                break   











