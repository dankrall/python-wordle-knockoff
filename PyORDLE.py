# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:08:07 2022

@author: dan
@"5-Word Dictionary, Stolen From": Wordle / Powerlanguage.co.uk 
https://www.powerlanguage.co.uk/wordle/
Run in Python3, its 2022 afterall. 
"""
import random

class Pyordle:

    def __init__(self):
        self.greeting = "Welcome to PyORDLE, a hastily copied commandline version of the popular game Wordle (now owned by NYT)"
        # this is where I'll set the word of the instance 
        # call a random number, access the file on read-line (randomnumber)
        # then set the attribute of the instance for the word
        f = open("Dictionary.txt", "r")
        content = f.readlines()
        dLN = len(content)
        ranSeed = random.randrange(0,dLN)
        self.theWord = content[ranSeed].upper()
                
    def circle(self):
        board = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []} #symptom of being under the influence. wasn't working unless I did this
        guesses = {1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}
        i = 1
        while i <= 6:
            print("\n")
            tryWordCap = input("Try #{} - Input a five letter word:  ".format(i))
            tryWord = tryWordCap.upper()
            guesses[i] = tryWord
            if len(tryWord) != 5:
                print("Please input a _FIVE_ letter word:")
            elif len(tryWord) == 5:
                if i == 6:
                    if tryWord == self.theWord:
                        print("\n")
                        print("Congrats, you finally got it.")
                        break
                    else:
                        print("\n")
                        print("Sorry, it looks like you got it wrong. The word was: {}".format(self.theWord))
                        
                i += 1
                if tryWord == self.theWord:
                    print("\n")
                    print("Congrats! You got the correct word {}, in {} tries. Good job you.".format(i-1, self.theWord))
                    break
                else:
                    retStr = []
                    for x in range(0, len(tryWord)):
                        if tryWord[x] == self.theWord[x]:
                            retStr.append(tryWord[x].upper())
                        elif tryWord[x] in self.theWord:
                            retStr.append(tryWord[x].lower())
                        else:
                            retStr.append("_")
                q = i - 1
                board[q] = retStr
                print("\n")
                for m in range(1, i):
                    print("     Try #{}: {}     Word: {}".format(m, board[m], guesses[m]))
                print("\n")
                print("Capital Letters are letters in the correct location")
                print("Lowercase Letters are within the word, but not the correct location")
                print("-------------------------------------------------------------------")


today = Pyordle()
print(today.greeting)
today.circle()

