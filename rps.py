"""
Rock, Paper, Scissors Game
Make a rock-paper-scissors game where it is the player vs the computer. 
The computer’s answer will be randomly generated, while the program will ask the user for their input. 
This project will better your understanding of while loops and if statements.
"""
import random

pc_rps = random.randrange(1,4,1)
#1 = rock
#2 = paper
#3 = scissors

user_rps = input("Enter R for rock, P for'paper' or S for 'scissors'")

if user_rps == "R" or "r" or "rock":
    user_rps = 1
elif user_rps == 'P' or 'p' or 'paper':
    user_rps = 2
elif user_rps == 'S' or 's' or 'scissors':
    user_rps = 3
else:
    print("Undetected selection")


if (user_rps == 1 and pc_rps == 3) or (user_rps == 2 and pc_rps == 1) or (user_rps == 3 and pc_rps == 2):
    print("You won" + str(pc_rps))
elif user_rps == pc_rps:
    print("It's a draw" + str(pc_rps))
else:
    print("You lost" + str(pc_rps))






