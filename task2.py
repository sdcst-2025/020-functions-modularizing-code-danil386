"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

import random

def title():
    print("Rock, Paper, Scissors")
    print("Instructions: When prompted, enter either rock, paper, or scissors. Rock beats scissors, paper beats rock, and scissors beats paper. The goal of the game is to beat the computer, who will make a random choice between the three every time.")

def game():
    options = ["rock", "paper", "scissors"]
    pchoice = input("Enter rock, paper or scissors: ")
    cchoice = random.choice(options)
    print(f"The computer chose {cchoice}")
    if (pchoice == "scissors" and cchoice == "rock") or (pchoice == "rock" and cchoice == "paper") or (pchoice == "paper" and cchoice == "scissors"):
        print("You Lost")
    elif pchoice == cchoice:
        print("Draw")
    else:
        print("You win")


title()
game()