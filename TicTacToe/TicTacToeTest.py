import unittest
from TicTacToeBoard import *

class MyTestCase(unittest.TestCase):
    def test_pos_moves(self):
        passed = True
        board = TicTacToeBoard("fish", "queen")
        correct_ans = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        if correct_ans == board.get_empty_spaces():
            print("passed basic test")
        else:
            passed = False
            print("Failed basic test")
        board.board = [player1_symbol] * 9
        if not board.get_empty_spaces():
            print("passed board is full case")
        else:
            passed = False
            print("Failed board is full case")
        board.board = [player1_symbol] + [player2_symbol] + [EMPTY] * 7
        if correct_ans[2:] == board.get_empty_spaces():
            print("passed first 2 not empty test")
        else:
            passed = False
            print("Failed first 2 not empty test")
        self.assertEqual(True, passed)



if __name__ == '__main__':
    unittest.main()
