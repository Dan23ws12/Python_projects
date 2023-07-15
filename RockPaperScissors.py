#U vs computer in a game of rock paper scissors
import random

def play():

    cont = "y"
    while (cont == "y") or (cont == "Y"):
        compStr = comp_play()
        inputStr = user_play()
        winner(inputStr, compStr)
        cont = input("press y to play again, anything else to cancel")


# determines the printed message given the plays made by the user and computer
def winner(user, comp):
    if user == comp:
        print("draw")
    elif user == "r":
        if comp == "s":
            print("user wins")
        else:
            print("computer wins")
    elif user == "s":
        if comp == "r":
            print("computer wins")
        else:
            print("user wins")
    else:
        if comp == "r":
            print("user wins")
        else:
            print("computer wins")

# chooses a random play for the computer
def comp_play():
    return random.choice(["r", "p", "s"])


def user_play():
    inputStr = input("enter r for rock, p for paper, and s for scissors")
    while (inputStr != "s") & (inputStr != "r") & (inputStr != "p"):
        print("wrong input")
        inputStr = input("enter r for rock, p for paper, and s for scissors")
    return inputStr


if __name__ == "__main__":
    play()