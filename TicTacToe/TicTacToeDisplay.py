import os

import pygame
import TicTacToeBoard
from TicTacToePlayer import *

"""
TicTacToe Display:
The screen is made up of 10 64 * 64 pixel tiles, each tile is either colored or contained a picture
"""
tile_size, num_tiles = 64, 10
screen_size = (tile_size * num_tiles, tile_size * num_tiles)  # width, height of the screen
screen_color = (0, 204, 204)  # rgb coordinates rep color of screen
screen = pygame.display.set_mode(screen_size)
board_by_row = [(3 * tile_size, 4 * tile_size), (4 * tile_size, 4 * tile_size), (5 * tile_size, 4 * tile_size),
                (3 * tile_size, 5 * tile_size), (4 * tile_size, 5 * tile_size), (5 * tile_size, 5 * tile_size),
                (3 * tile_size, 6 * tile_size), (4 * tile_size, 6 * tile_size), (5 * tile_size, 6 * tile_size)]
board_row_2 = [(3 * tile_size, 5 * tile_size), (4 * tile_size, 5 * tile_size), (5 * tile_size, 5 * tile_size)]
board_row_3 = [(3 * tile_size, 6 * tile_size), (4 * tile_size, 6 * tile_size), (5 * tile_size, 6 * tile_size)]
"""
Each player's symbol have been scaled to have width and height of a tile, the board_by_row variable
store the top left coordinate given to screen.blit
To display a player's symbol on row i column j, top left is  stored in index (i - 1)*3 + (j-1)
"""
player1_sym_img = pygame.transform.scale(pygame.image.load("./images/player1_symbol.png"), (tile_size, tile_size))
player2_sym_img = pygame.transform.scale(pygame.image.load("./images/player2_symbol.png"), (tile_size, tile_size))
logo_img = pygame.transform.scale(pygame.image.load("./images/logo.gif"), (tile_size * 6, tile_size))


def run(board):
    """
    :param board:
    """
    running, winner = True, ""
    clock = pygame.time.Clock()
    clock.tick(60)
    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (board.get_status() != TicTacToeBoard.NOT_OVER):
                running = False
            elif board.get_status() != TicTacToeBoard.NOT_OVER:
                running = False
            else:
                update_display(board)
                turn = board.get_turn()
                print("It's " + turn.get_name() + " turn")
                TicTacToeBoard.valid_play(board)
                winner = board.game_status()
    if board.get_status() == TicTacToeBoard.DRAW:
        print("the game ended in a draw")
    else:
        print(winner.get_name() + " won !")

def update_display(board):
    paint_screen()
    paint_board()
    paint_symbols(board)
    pygame.display.update()

def paint_screen():
    """
    paints the backgrounds and the logo
    """
    ins_surf_size = (tile_size * 6, tile_size * 6)
    inside_surf = pygame.Surface(ins_surf_size)
    surf_coord = (tile_size * 2, tile_size * 2)
    ins_surf_color = (160, 160, 160)

    logo_coord = (tile_size * 2, 0)
    inside_surf.fill(ins_surf_color)
    screen.fill(screen_color)
    screen.blit(inside_surf, surf_coord)
    screen.blit(logo_img, logo_coord)


def paint_board():
    """
    paints the TicTacToe board/table
    """
    table_line_sizes = [(tile_size * 3, 2), (2, tile_size * 3)]  # horizontal and vertical line sizes
    line_col = (255, 255, 255)
    for i in range(2):
        hor_line, vert_line = pygame.Surface(table_line_sizes[0]), pygame.Surface(table_line_sizes[1])
        hor_line.fill(line_col)
        vert_line.fill(line_col)
        screen.blit(hor_line, (tile_size * 3, tile_size * (5 + i)))
        screen.blit(vert_line, (tile_size * (4 + i), tile_size * 4))


def paint_symbols(board):
    """
    :param board: A TicTacToeBoard object
    when a player plays (places their symbol on a spot) this function draws that player's symbol on that spot
    in the board on the screen
    """
    txt, txt_coord = "player 1: X", (tile_size * 2, tile_size)
    txt_font_size = 17
    txt_display(screen, txt, txt_coord, txt_font_size)
    txt, txt_coord = "player 2: O", ((tile_size * 6) + 20, tile_size)
    txt_display(screen, txt, txt_coord, txt_font_size)
    index, board_spots = 0, board.get_board()
    for coord in board_by_row:
        if board_spots[index] == TicTacToeBoard.player1_symbol:
            screen.blit(player1_sym_img, coord)

        elif board_spots[index] == TicTacToeBoard.player2_symbol:
            screen.blit(player2_sym_img, coord)
        index += 1


# a function to help debug and make things fit in the tiles
def paint_lines():
    line_col = (0, 0, 0)
    x_line_size = (2, screen_size[1])
    y_line_size = (screen_size[0], 2)
    for i in range(num_tiles):
        x_line = pygame.Surface(x_line_size)
        y_line = pygame.Surface(y_line_size)
        y_line.fill(line_col)
        x_line.fill(line_col)
        screen.blit(x_line, (i * tile_size, 0))
        screen.blit(y_line, (0, i * tile_size))


def txt_display(canvas, message, coord, font_size, col=(0, 0, 0), font="Comic Sans Ms"):
    """
    :param font_size: int size of the font of msg
    :param canvas: a surface to paint the message over (usually screen)
    :param message: the message to be printed
    :param coord: the point on the canvas the message should start at
    :param col: color the message should be painted in
    :param font:the font the massage should be painted in
    This function takes a message and prints the message on the given canvas
    """
    dis_font = pygame.font.SysFont(font, font_size, False)
    head_txt_surface = dis_font.render(message, False, col)
    canvas.blit(head_txt_surface, coord)
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    player1 = Player(TYPE_USER, "sans")
    player2 = Player(TYPE_USER, "elk")
    print(os.getcwd())
    board2 = TicTacToeBoard.TicTacToeBoard(player1, player2)
    board2.board = ([TicTacToeBoard.player1_symbol] * 2) + [TicTacToeBoard.player2_symbol] + [
        TicTacToeBoard.player1_symbol] * 6
    # display(board2)
