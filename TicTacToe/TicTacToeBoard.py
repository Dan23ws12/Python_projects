import TicTacToePlayer

NOT_OVER, DRAW, WON = 0, 1, 2
player1_symbol, player2_symbol = "X", "O"
player1_win_cond, player2_win_cond = player1_symbol * 3, player2_symbol * 3
NO_WINNER, EMPTY = TicTacToePlayer.Player(TicTacToePlayer.TYPE_USER, "NO WINNER"), "_" #

class TicTacToeBoard:
    """
    This class represents the TicTacToe board,
    It contains a list representing the board, the names of the players, status of the game, number of
    empty spaces left and whose turn it is to play.
    The board is looks like this:
    col     1  2   3
    row1:  X | O | X
    row2:  O | X | O
    row3:  _ | _ | X
    index 0 of the list represents row1 and column 1 or (1, 1) (top left), index 1 represents row 1 column 2
    or (1, 2) (top middle) index 3 of the list is row 2 column 1 or (2, 1) and so on
    """
    def __init__(self, player1, player2):
        self.board = [EMPTY] * 9
        self.player1 = player1
        self.player2 = player2
        self.num_empty = 9
        self.status = NOT_OVER
        self.turn = player1

    def get_status(self):
        return self.status

    def get_board(self):
        return self.board

    def get_turn(self):
        return self.turn

    def get_num_empty(self):
        return self.num_empty

    def get_player1(self):
        return self.player1

    def get_player2(self):
        return self.player2

    def get_empty_spaces(self):
        """
        Returns a list of all possible moves left on this board represented by tuples
        """
        pos_moves = []
        for index in range(0, 9):
            if self.board[index] == EMPTY:
                row = index // 3 + 1
                column = index % 3 + 1
                # 1// 3 + 1 = 0 + 1, thus row 1, 1%3 + 1 = 1 + 1 thus giving column 2 , thus index 1 -> (1, 2)
                pos_moves.append(tuple([row, column]))
        return pos_moves

    def game_status(self):
        """
        If the game was won, this function updates the status of the game and returns name of the player
        who won the game, returns _ if game was not won or the game ended in a draw.
        If game ended in a draw, game status is changed to draw
        """
        winner = self.check_row_col()
        if winner != NO_WINNER:
            return winner
        winner = self.check_diagonals()
        if winner != NO_WINNER:
            return winner
        if self.num_empty == 0:
            self.status = DRAW
        return NO_WINNER

    def check_row_col(self):
        """
        :return: returns the Player Object representing who won by filling a row or col with their symbol ,
        NO_WINNER otherwise
        """
        for index in range(3):
            # checks if a row  is filled with only X's or O's
            winner = self.is_win(self.board[3 * index: 3 * (index + 1)])
            if winner == NO_WINNER:  # if neither player has won, checks if a column is only filled with X's or O's
                winner = self.is_win(self.board[index: (index + 7): 3])
            if winner != NO_WINNER:  # if someone has won returns the name of winning player and changes game status
                self.status = WON
                return winner
        return NO_WINNER

    def check_diagonals(self):
        """
        :return: returns the Player Object representing who won by filling a diagonal with their symbol ,
        NO_WINNER otherwise
        """
        diagonals = [self.board[0:9:4], self.board[2:8:2]]
        for diagonal in diagonals:
            winner = self.is_win(diagonal)
            if winner != NO_WINNER:
                self.status = WON
                return winner
        return NO_WINNER

    def is_win(self, side):
        """
        If a player has filled the given side (which can be a row, column or diagonal) with only their symbol,
        returns the name of that player, returns the symbol for NO_WINNER otherwise
        :param side: a list of size 3 representing a row, column or diagonal
        """
        cond_check = "".join(side)
        if cond_check == player1_win_cond:
            return self.player1
        elif cond_check == player2_win_cond:
            return self.player2
        return NO_WINNER

    def play(self, row, col):
        """
        This function return "" if the space at the given row and column is free to play in and places the player's
        symbol, otherwise returns "NOT EMPTY"
        :param row: an integer between 1 and 3
        :param col: and integer between 1 and 3
        """
        play_spot = (row - 1)*3 + (col - 1)
        if (self.num_empty == 0) or self.board[play_spot] != EMPTY: #checks if the spot is available to be played
            return "NOT EMPTY"
        self.num_empty -= 1
        if self.turn == self.player1:
            self.board[play_spot] = player1_symbol
            self.turn = self.player2
        else:
            self.board[play_spot] = player2_symbol
            self.turn = self.player1
        return EMPTY

def valid_play(board):
    """
    This function takes a TicTacToe board and the name of the player who has yet to play
    and makes sure their play is valid
    """
    turn = board.get_turn()
    if turn.get_player_type() == TicTacToePlayer.TYPE_USER:  # checks if player is not a computer
        co_ords = user_move()
        while board.play(co_ords[0], co_ords[1]) != EMPTY:
            print("That spot has been taken")
            co_ords = user_move()
    else:
        co_ords = rand_comp_move()
        while board.play(co_ords[0], co_ords[1]) != EMPTY:
            print("That spot has been taken")
            co_ords = rand_comp_move()

def rand_comp_move():
    """
    This bot ai chooses moves randomly
    :return:
    """
    return random.randint(1, 3), random.randint(1, 3)

def user_move():
    """
    This function takes care of user input
    """
    xCoord = int(input("which row?: "))
    while (xCoord < 1) or (xCoord > 3):
        print("invalid input")
        xCoord = int(input("which row?: "))
    yCoord = int(input("which column?: "))
    while (yCoord < 1) or (yCoord > 3):
        print("invalid input")
        yCoord = int(input("which column?: "))
    return xCoord, yCoord

# Minimax AI stuff
def heuristic_function(board, this_player, is_max=True):
    """
    :param board:
    :param this_player:
    :param is_max:
    :return:
    """
    #TO BE COMPLETED
    pass


def utility_function(board, this_player, is_max=True):
    """
    :param board:
    :param this_player: the name of the player whose turn the game ended on
    :param is_max: True if this_player is max player aka MINIMAX AI
    :return:
    """
    winner = board.game_status()
    num_empty_spaces = board.get_num_empty()
    if winner == NO_WINNER:
        return 0
    if winner == this_player:
        if is_max is True:
            return num_empty_spaces
        return num_empty_spaces * -1
    elif is_max is True:
        return num_empty_spaces
    return num_empty_spaces
