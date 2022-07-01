myWord = input('Enter a word for Game:')
print(myWord)
wordList = list(myWord)

print(wordList) 
print(len(wordList))

emptyList = []
for i in range(len(wordList)):
    emptyList.append('_')

print(emptyList)


