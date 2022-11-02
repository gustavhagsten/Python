import os
import random

Animal_list = ["dog", "cow", "cat", "goose", "fox", "gorilla", "horse", "orangutan", "tiger"]

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


os.system('cls')
    
while True:

    if lives == 0:
        os.system("cls")
        print(HANGMANPICS[lives])
        print("\n")

        Print_letter()

        print("\n You Lost! \n \n " + "The right word was " +  rightword)
        break


    print(HANGMANPICS[lives])
    print("\n")


    Print_letter()


    guess = input("\n" + "Enter a letter: ")
    

    if guess in correct_letters:
        print("\n" + "Letter alredy guessed that!")
        os.system("cls")
        continue
    elif guess not in rightword:
        print("Wrong Letter!")
        lives = lives - 1
        os.system("cls")
        continue


    correct_letters = correct_letters + guess

    if sorted(rightword) == sorted(correct_letters):
        os.system("cls")
        print("\n" + "You Won!")
        break




    os.system('cls')