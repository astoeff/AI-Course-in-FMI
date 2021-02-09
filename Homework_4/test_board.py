#NOT WORKING TESTS
#TODO
import unittest

from constants import INITIAL_VERSION_OF_BOARD
from board import Board


class TestBoard(unittest.TestCase):
    #tests for check_if_solved_by_row()
    def test_with_given_empty_board_should_return_symbol_for_empty_position(self):
        #ASSET
        board = Board(INITIAL_VERSION_OF_BOARD)
        expected_sign = '_'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_first_row_with_xs_should_return_symbol_for_x(self):
        #ASSET
        board_as_list = [['X', 'X', 'X'], ['O', 'O', '_'], ['O', '_', '_']]
        board = Board(board_as_list)
        expected_sign = 'X'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_first_row_with_os_should_return_symbol_for_o(self):
        #ASSET
        board_as_list = [['O', 'O', 'O'], ['_', 'X', '_'], ['X', '_', 'X']]
        board = Board(board_as_list)
        expected_sign = 'O'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_second_row_with_xs_and_empty_first_row_should_return_symbol_for_x(self):
        #ASSET
        board_as_list = [['_', '_', '_'], ['X', 'X', 'X'], ['O', 'O', '_']]
        board = Board(board_as_list)
        expected_sign = 'X'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_second_row_with_os_and_empty_first_row_should_return_symbol_for_o(self):
        #ASSET
        board_as_list = [['_', '_', '_'], ['O', 'O', 'O'], ['X', 'X', '_']]
        board = Board(board_as_list)
        expected_sign = 'O'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_second_row_with_xs_and_non_empty_first_row_should_return_symbol_for_x(self):
        #ASSET
        board_as_list = [['_', '_', 'O'], ['X', 'X', 'X'], ['_', 'O', 'O']]
        board = Board(board_as_list)
        expected_sign = 'X'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_second_row_with_os_and_non_empty_first_row_should_return_symbol_for_o(self):
        #ASSET
        board_as_list = [['_', 'X', '_'], ['O', 'O', 'O'], ['_', 'X', 'X']]
        board = Board(board_as_list)
        expected_sign = 'O'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_third_row_with_xs_should_return_symbol_for_x(self):
        #ASSET
        board_as_list = [['_', '_', 'O'], ['_', 'O', '_'], ['X', 'X', 'X']]
        board = Board(board_as_list)
        expected_sign = 'X'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_with_given_solved_board_on_third_row_with_os_should_return_symbol_for_o(self):
        #ASSET
        board_as_list = [['_', '_', 'X'], ['_', 'X', '_'], ['O', 'O', 'O']]
        board = Board(board_as_list)
        expected_sign = 'O'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)
    
    #test check_if_solved_by_col()
    def test_check_if_solved_by_col_with_given_empty_board_should_return_symbol_for_empty_position(self):
        #ASSET
        board = Board(INITIAL_VERSION_OF_BOARD)
        expected_sign = '_'     

        #ACT
        result_sign = board.check_if_solved_by_col()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    def test_check_if_solved_by_col_with_given_solved_board_on_first_row_with_xs_should_return_symbol_for_x(self):
        #ASSET
        board_as_list = [['X', 'X', 'X'], ['O', 'O', '_'], ['O', '_', '_']]
        board = Board(board_as_list)
        expected_sign = 'X'     

        #ACT
        result_sign = board.check_if_solved_by_row()

        #ASSERT
        self.assertEqual(result_sign, expected_sign)

    # def test_with_given_solved_board_on_first_row_with_os_should_return_symbol_for_o(self):
    #     #ASSET
    #     board_as_list = [['O', 'O', 'O'], ['_', 'X', '_'], ['X', '_', 'X']]
    #     board = Board(board_as_list)
    #     expected_sign = 'O'     

    #     #ACT
    #     result_sign = board.check_if_solved_by_row()

    #     #ASSERT
    #     self.assertEqual(result_sign, expected_sign)

    # def test_with_given_solved_board_on_second_row_with_xs_and_empty_first_row_should_return_symbol_for_x(self):
    #     #ASSET
    #     board_as_list = [['_', '_', '_'], ['X', 'X', 'X'], ['O', 'O', '_']]
    #     board = Board(board_as_list)
    #     expected_sign = 'X'     

    #     #ACT
    #     result_sign = board.check_if_solved_by_row()

    #     #ASSERT
    #     self.assertEqual(result_sign, expected_sign)

    # def test_with_given_solved_board_on_second_row_with_os_and_empty_first_row_should_return_symbol_for_o(self):
    #     #ASSET
    #     board_as_list = [['_', '_', '_'], ['O', 'O', 'O'], ['X', 'X', '_']]
    #     board = Board(board_as_list)
    #     expected_sign = 'O'     

    #     #ACT
    #     result_sign = board.check_if_solved_by_row()

    #     #ASSERT
    #     self.assertEqual(result_sign, expected_sign)

    # def test_with_given_solved_board_on_second_row_with_xs_and_non_empty_first_row_should_return_symbol_for_x(self):
    #     #ASSET
    #     board_as_list = [['_', '_', 'O'], ['X', 'X', 'X'], ['_', 'O', 'O']]
    #     board = Board(board_as_list)
    #     expected_sign = 'X'     

    #     #ACT
    #     result_sign = board.check_if_solved_by_row()

    #     #ASSERT
    #     self.assertEqual(result_sign, expected_sign)

    # def test_with_given_solved_board_on_second_row_with_os_and_non_empty_first_row_should_return_symbol_for_o(self):
    #     #ASSET
    #     board_as_list = [['_', 'X', '_'], ['O', 'O', 'O'], ['_', 'X', 'X']]
    #     board = Board(board_as_list)
    #     expected_sign = 'O'     

    #     #ACT
    #     result_sign = board.check_if_solved_by_row()

    #     #ASSERT
    #     self.assertEqual(result_sign, expected_sign)

    # def test_with_given_solved_board_on_third_row_with_xs_should_return_symbol_for_x(self):
    #     #ASSET
    #     board_as_list = [['_', '_', 'O'], ['_', 'O', '_'], ['X', 'X', 'X']]
    #     board = Board(board_as_list)
    #     expected_sign = 'X'     

    #     #ACT
    #     result_sign = board.check_if_solved_by_row()

    #     #ASSERT
    #     self.assertEqual(result_sign, expected_sign)

    # def test_with_given_solved_board_on_third_row_with_os_should_return_symbol_for_o(self):
    #     #ASSET
    #     board_as_list = [['_', '_', 'X'], ['_', 'X', '_'], ['O', 'O', 'O']]
    #     board = Board(board_as_list)
    #     expected_sign = 'O'     

    #     #ACT
    #     result_sign = board.check_if_solved_by_row()

    #     #ASSERT
    #     self.assertEqual(result_sign, expected_sign)
    # 