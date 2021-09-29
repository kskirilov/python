"""
Hangman Game
This is probably the hardest one out of these 6 small projects. 
This will be similar to guessing the number, except we are 
guessing the word. 
The user needs to guess letters,
Give the user no more than 6 attempts for guessing wrong letter. 
This will mean you will have to have a counter. 
You can download a ‘sowpods’ dictionary file or csv file to use as 
a way to get a random word to use.
"""
import random
#Load csv file with words, convert to array

words = ["body", "tower", "human", "license", "water", "bus", "bicycle", "lemon"]
#Randomly select word from array
hangman_word = words[random.randrange(1, len(words), 1)]
attempts = 6

#selected word example tower
#how to get letters of word
#should I give away first and last letter in official hangman rules?
#(keep it simple for now and don't)
guessArray = []

guess = input("The word is: " + "_ " * len(hangman_word) + "     Attempts remaining: " + str(attempts) + "\n"
+ "Letters used: " + guessArray)
#Change letter in word "_ _ _ _ _ _ "
hangman_word.find('guess') #this will give us the position of the word
while attempts>0:
    #If guess is correct, loop over the hidden underscores and display all words that match the word
        #1. Check letter is in word.
        #2. 
    if guess in hangman_word:
        guessArray.append(guess)
        guess = input("Correct. Guess next one!")
    else:
        attempts = attempts - 1
        guess = input("Incorrect. Guess a letter in the word")

print("Game is over. The word was: "+ hangman_word)


















