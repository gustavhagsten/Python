import os
import random

Animal_list = ["dog", "cow", "cat", "fox", "horse", "tiger"]

rightword = random.choice(Animal_list)

correct_letters = ""

lives = 3

HANGMANPICS = { 3: '''
  +---+
  |   |
      |
      |
      |
      |
=========''', 2: '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 1: '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 0: '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''}


def Print_letter():
    for letter in rightword:
        if letter in correct_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")



# Start game with clear terminal.
os.system('cls')

while True:

    # Live checker
    # If lives hit 0, the player loose the game.
    if lives == 0:
        os.system("cls")
        print(HANGMANPICS[lives])
        print("\n")
        Print_letter()
        print("\n")
        print("You Lost! \n \n" + "The right word was " +  rightword + "\n")
        break


    print(HANGMANPICS[lives])
    print("\n")

    Print_letter()
    print("\n")


    guess = input("Enter a letter: ")

    # Check if the guess is correct or not.
    if guess in correct_letters:
        os.system("cls")
        continue
    elif guess not in rightword:
        lives = lives - 1
        os.system("cls")
        continue


    correct_letters = correct_letters + guess


    # Check if all letters was guessed
    if sorted(rightword) == sorted(correct_letters):
        os.system("cls")
        print("\n" + "You Won!")
        break


    # Clear terminal
    os.system('cls')