import random
hangman = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
========='''
]

wordList = ['sky','river','shadow','echo','journey','whisper','thunder','spark','feather','horizon']
word = random.choice(wordList)
wordLen = len(word)
display=""
for letter in range(0,wordLen):
    display+="_"
print("Welcome to the Hangman Game\n")
print("This is the word: ",display)
print(hangman[6])

lives=6
gameOver = False
varList=[]
while not gameOver:
    userInput=input("Enter your guess: \n")
    userInput=userInput.lower()
    display=""
    for letter in word:
        if letter == userInput:
            print(f"{userInput} is a correct guess.\n")
            display += letter
            varList.append(letter)
        elif letter in varList:
            display += letter
        else:
            display += "_"
    print(display)
    if userInput not in word:
        lives -= 1
        if lives == 0:
            gameOver = True
            print("You Lost.")
            print("The word was: ",word)
    if "_" not in display:
        gameOver = True
        print("You Win.")
    print(hangman[lives])