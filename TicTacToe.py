import random

# An implementation of the game of tictactoe


ticTacToeBoard = ["_" for x in range(9)]
game_not_over, draw = "NO ONE WINS!!!", "draw!!!"
def gamestatuscheck():
    row1, col1= "".join(ticTacToeBoard[:3]), "".join(ticTacToeBoard[:7:3])
    row2, col2 = "".join(ticTacToeBoard[3:6]), "".join(ticTacToeBoard[1:8:3])
    row3, col3 = "".join(ticTacToeBoard[6:]), "".join(ticTacToeBoard[2:9:3])
    diag1, diag2 = "".join(ticTacToeBoard[0:9:4]), "".join(ticTacToeBoard[2:8:2])
    player1WinCon, player2WinCon = "X" * 3, "O" * 3
    isEmptyRowSpace = ("_" in row1) or ("_" in row2) or ("_" in row3)
    isEmptyColSpace = ("_" in col1) or ("_" in col2) or ("_" in col3)
    isEmptyDiagSpace = ("_" in diag1) or ("_" in diag2)
    if (row1 == player1WinCon) or (col1 == player1WinCon) or (row2 == player1WinCon) or (col2 == player1WinCon)\
            or (row3 == player1WinCon) or (col3 == player1WinCon) or (diag1 == player1WinCon) or (diag2 == player1WinCon):
        return player_1_wins
    elif (row1 == player2WinCon) or (col1 == player2WinCon) or (row2 == player2WinCon) or (col2 == player2WinCon)\
            or (row3 == player2WinCon) or (col3 == player2WinCon) or (diag1 == player2WinCon) or (diag2 == player2WinCon):
        return player_2_wins
    elif isEmptyDiagSpace or isEmptyColSpace or isEmptyRowSpace:
        return game_not_over
    else:
        return draw


def tictactoe():
    print("we are going to play a game of tic tac toe")
    gameOver, turn = False, player_1_name
    gameStatus = ""
    while gameOver is False:
        printBoard()
        if turn == player_1_name:
            print(player_1_name + "'s turn")
            gameOver, gameStatus = play(player_1_name)
            turn = player_2_name
        else:
            turn = player_1_name
            print(player_2_name + "'s turn")
            gameOver, gameStatus = play(player_2_name)
    print(gameStatus)
    print("good game")






def play(whoseturn):
    """
    this method takes a string representing which player's turn it is, handles how the player places their
    X or O in any spot they please, and returns a tuple containing a boolean value representing whether the
    game is over or not and who won the game.
    """
    if whoseturn != "COMPUTER":
        xCoord = int(input("which row do u want to play? "))  # which row the player wants to place their piece
        yCoord = int(input("which column do u want to play? "))  # which column the player wants to place their piece
        while ticTacToeBoard[(3 * (xCoord - 1)) + (yCoord - 1)] != "_":  # doesn't allow a player to place an X or O in a taken spot
            print("that spot is already taken")
            xCoord = int(input("which row do u want to play? "))
            yCoord = int(input("which column do u want to play? "))
    else:
        xCoord = random.randint(1, 3)
        yCoord = random.randint(1, 3)
        while ticTacToeBoard[(3 * (xCoord - 1)) + (yCoord - 1)] != "_":
            xCoord = random.randint(1, 3)
            yCoord = random.randint(1, 3)
    if whoseturn == player_1_name:
        ticTacToeBoard[(3 * (xCoord - 1)) + (yCoord - 1)] = "X"
    else:
        ticTacToeBoard[(3 * (xCoord - 1)) + (yCoord - 1)] = "O"
    gameStatus = gamestatuscheck()
    if gameStatus != game_not_over:
        return True, gameStatus
    return False, game_not_over

def namePlayers():
    """
    returns the typed names of the two players
    """
    player1 = input("type the name of player 1: ")
    playVComp = input("press y if u want to play against computer ").lower()
    if playVComp == "y":
        player2 = "COMPUTER"
    else:
        player2 = input("type the name of player 2")
    return player1, player2

def printBoard():
    print(ticTacToeBoard[:3])
    print(ticTacToeBoard[3:6])
    print(ticTacToeBoard[6:])


player_1_name, player_2_name = namePlayers()
player_1_wins, player_2 = player_1_name + " wins!!!", player_2_name + " wins!!!"
if __name__ == "__main__":
    tictactoe()