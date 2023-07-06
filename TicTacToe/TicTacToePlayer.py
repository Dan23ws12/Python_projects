import random
TYPE_USER, TYPE_RAND_BOT = "USER", "RANDOM COMPUTER" #the type constants for user and random AI respectively


class Player:
    """
    A class representing the players in a TicTacToe game.
    Players have two attributes, name of the player and type.
    If the player is a bot/robot (type robot) then the name will be random
    computer (means this bot picks moves at random) or
    minimax ai (this bot searches through all moves abd picks the best one)
    """
    def __init__(self, player_type, name):
        self.player_type = player_type
        self.name = name


    def get_name(self):
        return self.name

    def get_player_type(self):
        return self.player_type

    def player_move(self):
        """
        :return: returns the move (row and column) this player just made
        """
        if self.player_type == TYPE_USER:
            return user_move()
        else: # if the player isn't a user, it's a bot
            return rand_comp_move()
        # elif self.name == RANDOM_COMP
        # minimax AI has not been implemented yet

    def __eq__(self, other):
        return (self.name == other.name) and (self.player_type == other.player_type)

    def __str__(self):
        return self.name