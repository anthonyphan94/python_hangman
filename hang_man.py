# # myWord = input('Enter a word for Game:')
# # print(myWord)
from tkinter import W


myWord = 'computerc'
wordList = list(myWord)
life = 6 
print(wordList)


displayList = []
for i in range(len(wordList)):
    displayList.append('_')

print(displayList)


end_of_game = False
while not end_of_game:

    guessWord = input('Please Enter your guess: ')
    for i in range(len(wordList)):
        letter = wordList[i]
        if guessWord == letter:
            displayList[i] = letter

    # to check word not in wordList, has to stay outside of for loop
    # otherwise, it will print out many word in the list
    if guessWord not in wordList:
        life -= 1
    if life == 0:
        end_of_game = True
        print('you lost')

    print(displayList)

    if "_" not in displayList:
        end_of_game = True   
        print('win')

