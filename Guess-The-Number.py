"""
Write a programme where the computer randomly generates a number between 0 and 20. 
The user needs to guess what the number is. If the user guesses wrong, 
tell them their guess is either too high, or too low. This will get you started with 
the random library if you haven't already used it.
--v3--Added classes and methods.

Use .ipynb to make a jupyter notebook file.
"""
import random

class GuessingGame:

    #def __init__(self, guess):
    #    self.guess = guess

    def start():
        randNum = random.randrange(1,20,1)
        guess = input("enter a number")

        while int(guess) != randNum:
            if int(guess)<1 or int(guess)>20:
                print("Your guess is outside of the required range. The range is 1 to 20.")
                guess = input("Guess number between 1 and 20 \n")
            elif int(guess) < randNum:
                print("Sorry, your guess is lower than the random number. Give it another try: ")
                guess = input("Guess number between 1 and 20 \n")
            else:
                print("Sorry, your guess is higher than the random number. Give it another try: ")
                guess = input("Guess number between 1 and 20 \n")
        print("Congratulations, your guess is correct!")    


GuessingGame.start()