# an implementation of the Hangman game
import random

def Hangman():
    """
    this method handles the main loop of the game
    """
    wordList = ["faith", "speed", "run", "pity"]  # list of random words
    replay = input("do u want to play a hangman game? if so press y").lower()
    while replay == "y":
        word = random.choice(wordList)  # a random word chosen from a list of words
        print("can u guess a " + str(len(word)) + " character long word to save a man's life?")
        print("_"*len(word))
        handleGuess(word)
        replay = input("do u want to play again? If so press y").lower()


def handleGuess(word):
    """
    this method handles the guessing part of the game.
    """
    death, noGuessUsed = 10, 0
    length = len(word)
    guessedRight, guessWord = False, "_"*length
    while (noGuessUsed < death) and (guessedRight is False):
        guess = input()  # the guessed letter
        if (word.find(guess) != -1) and (guessWord.find(guess) == -1):
            for i in range(length):
                if word[i] == guess:
                    guessWord = guessWord[:i] + guess + guessWord[i + 1:]
        else:
            noGuessUsed += 1
        if guessWord == word:
            guessedRight = True
        print(guessWord)

    if guessedRight is False:
        print(" couldn't guess the correct word")
    else:
        print("the innocent man survived")


if __name__ == "__main__":
    Hangman()
