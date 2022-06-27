#Dice Roll Simulator project
import random


def diceRollSimulator():
    """
    This function makes the computer roll dice (random number from 1 to 6) and asks the user
    if the computer should reroll and, if requested the computer rerolls until user says
    anything but yes
    :return: Nothing
    """
    retry = "y"
    while (retry == "y"):
        roll = str(random.randint(1, 6))
        print("the computer rolled the number " + roll)
        retry = input("press y to make computer roll again")


if __name__ == "__main__":
    diceRollSimulator()