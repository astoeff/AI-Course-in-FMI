import unittest

from puzzle_node import Puzzle_node
from main import iterative_deepening_a_star

class TestIterativeDeepeningAStar(unittest.TestCase):
    def test_with_given_3_x_3_puzzle_and_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3], [0, 5, 6], [4, 7, 8]]
        position_of_zero_in_given_puzzle = (1, 0)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        position_of_zero_in_final_state = (2, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 3
        #list of reversed directions
        expected_directions = ['left', 'left', 'up']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_4_x_4_puzzle_and_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4], [0, 6, 7, 8], [5, 10, 11, 12], [9, 13, 14, 15]]
        position_of_zero_in_given_puzzle = (1, 0)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        position_of_zero_in_final_state = (3, 3)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 5
        #list of reversed directions
        expected_directions = ['left', 'left', 'left', 'up', 'up']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_5_x_5_puzzle_and_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [0, 17, 18, 19, 20], [16, 21, 22, 23, 24]]
        position_of_zero_in_given_puzzle = (3, 0)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
        position_of_zero_in_final_state = (4, 4)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 5
        #list of reversed directions
        expected_directions = ['left', 'left', 'left', 'left', 'up']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)
