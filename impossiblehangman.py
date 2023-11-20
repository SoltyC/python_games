# bug: press same letter and still correct. can be abused to skip letters in a word to get it correct.

import random

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
words = 'airport airbus boeing python lockheed stealth jet fighter pilot fuel sky gear glide navigation wing flight'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    misses = len(missedLetters)
    if misses > 6:
        misses = 6
    print(HANGMAN_PICS[misses])
    print()
    print("_ " * len(secretWord))
    print()
    print('Correct letters:', end=' ')
    for letter in correctLetters:
        print(letter, end=' ')
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    print()

def main():
    print('H A N G M A N AVIATION EDITION')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = False

    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('Hey! What letter is next?')
        guess = input().lower()
        if len(guess) > 0 and guess in secretWord:
            correctLetters = correctLetters + guess
            print('You got the letter correct!')
            if len(secretWord) == len(correctLetters):
                print('Oh my god! You are so good at guessing aircraft stuff. You are a good person!')
                break
            
        else:
            print('Failiure management always needed you!')
            missedLetters = missedLetters + guess
            if len(missedLetters) >= 6:
                print('You suck. You lost. Ha Ha! You will never beat me >:)')
                break
            

    print('Thank you for playing! The word was: ' + secretWord + "!")
    print('Would you like to play again? Press y to continue :)')
    if input() == "y":
        main()
main()
