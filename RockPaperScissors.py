#U vs computer in a game of rock paper scissors
import random

def play():
    inputStr = input("enter r for rock, p for paper, and s for scissors")
    while (inputStr != "s") & (inputStr != "r") & (inputStr != "p"):
        print("wrong input")
        inputStr = input("enter r for rock, p for paper, and s for scissors")
    compStr = random.choice(["r", "p", "s"])
    if inputStr == "r":
        if compStr == "r":
            print("draw")
        elif compStr == "s":
            print("user wins")
        else:
            print("computer wins")
    elif inputStr == "s":
        if compStr == "r":
            print("computer wins")
        elif compStr == "s":
            print("draw")
        else:
            print("user wins")
    else:
        if compStr == "r":
            print("user wins")
        elif compStr == "s":
            print("computer wins")
        else:
            print("draw")


if __name__ == "__main__":
    play()