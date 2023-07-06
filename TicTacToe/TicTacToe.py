
# An implementation of the game of tictactoe
import TicTacToeBoard
import TicTacToeDisplay
import TicTacToePlayer
import pygame

pygame.init()
pygame.font.init()
RANDOM_COMP = "rand comp"
MINIMAX_AI = "unbeatable"


def tictactoe():
    print("We are going to play a game of tic tac toe")
    player1, player2 = get_players()
    board = TicTacToeBoard.TicTacToeBoard(player1, player2)
    TicTacToeDisplay.run(board)
    print("good game")

def get_players():
    """
    returns a tuple of Player Objects, first and second object represent player1 and player2 respectively
    """
    player1_name = get_player_name()
    player1 = TicTacToePlayer.Player(TicTacToePlayer.TYPE_USER, player1_name)
    playVComp = input("press y if u want to play against computer ").lower()
    player2_name = get_player_name(player1_name)
    if playVComp == "y":
        player2 = TicTacToePlayer.Player(TicTacToePlayer.TYPE_RAND_BOT, player2_name)
    else:
        player2 = TicTacToePlayer.Player(TicTacToePlayer.TYPE_USER, player2_name)
    return player1, player2

def get_player_name(player1_name=""):
    """
    :return: Returns a Player Object representing a user
    """
    player_name = input("type the name of player : ")
    while (player_name == TicTacToeBoard.NO_WINNER.get_name()) \
            or (player_name == player1_name) or (player_name == ""):
        print("this name is taken")
        player_name = input("type the name of player : ")
    return player_name


if __name__ == "__main__":
    tictactoe()