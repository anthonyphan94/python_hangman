from hang_man_wordList import animalList
from tkinter import W
import random
from os import system
from hang_man_art import logo, stages

# Print Hangman Logo
print(logo)
print(stages[6])
#Pick a random word from the list and generate the empty word
myWord = random.choice(animalList)
wordList = list(myWord)
life = 6 
print(myWord, "\n")
displayList = []
for i in range(len(wordList)):
    displayList += '_'
print(" ".join(displayList), "\n")


#main game
end_of_game = False

while not end_of_game:

    guessWord = input('Please Enter your guess: ')
    # system('clear')

    # Check if word in word list
    for i in range(len(wordList)):
        letter = wordList[i]
        if guessWord == letter:
            displayList[i] = letter

    # to check word not in wordList, has to stay outside of for loop
    # otherwise, it will print out many word in the list
    if guessWord not in wordList:
        life -= 1
        print('\nWrong Guess, please try again, You have  {first} life left.'.format(first=life))
        print(stages[life])
  
    if life == 0:
        end_of_game = Trupe
        print('you lost\n')

    print(" ".join(displayList), "\n")
    #Check if the word is filled
    if "_" not in displayList:
        end_of_game = True   
        print('You Win,Congratulation!\n')


