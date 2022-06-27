#Guess number game project
import random

def compGuessNum():
    """
    This method gets user to enter a number from 1 to 10 and prints the number of tries the computer
    takes to guess the number the user entered
    """
    intInput = int(input("Input an integer from 1 to 10: "))
    while (intInput > 10) | (intInput < 1):
        print("input not in range")
        intInput = int(input("Input an integer from 1 to 10: "))
    compGuess = random.randint(1, 11)
    index = 2
    guessRght = False
    if compGuess == intInput:
        print("the computer guessed what u entered after 1 try")
    while guessRght is False:
        compGuess = random.randint(1, 11)
        prntStr = "the computer guessed what u entered after {} try"
        if compGuess == intInput:
            print(prntStr.format(index))
            guessRght = True
        else:
            index += 1


if __name__ == "__main__":
    compGuessNum()