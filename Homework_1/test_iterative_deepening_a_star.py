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

    def test_with_given_3_x_3_puzzle_and_not_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3], [4, 5, 8], [6, 7, 0]]
        position_of_zero_in_given_puzzle = (2, 2)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        position_of_zero_in_final_state = (1, 0)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 3
        #list of reversed directions
        expected_directions = ['right', 'right', 'down']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_4_x_4_puzzle_and_not_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4], [5, 6, 7, 11], [8, 9, 10, 0], [12, 13, 14, 15]]
        position_of_zero_in_given_puzzle = (2, 3)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3, 4], [5, 6, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        position_of_zero_in_final_state = (1, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 2
        #list of reversed directions
        expected_directions = ['right', 'down']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_5_x_5_puzzle_and_not_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4, 5], [6, 7, 0, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        position_of_zero_in_given_puzzle = (1, 2)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        position_of_zero_in_final_state = (2, 4)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 2
        #list of reversed directions
        expected_directions = ['left', 'left']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_3_x_3_solved_puzzle_and_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        position_of_zero_in_given_puzzle = (2, 2)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        position_of_zero_in_final_state = (2, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 0
        #list of reversed directions
        expected_directions = []

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_4_x_4_solved_puzzle_and_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        position_of_zero_in_given_puzzle = (3, 3)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        position_of_zero_in_final_state = (3, 3)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 0
        #list of reversed directions
        expected_directions = []

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_5_x_5_solved_puzzle_and_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
        position_of_zero_in_given_puzzle = (4, 4)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board =[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
        position_of_zero_in_final_state = (4, 4)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 0
        #list of reversed directions
        expected_directions = []

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_3_x_3_solved_puzzle_and_not_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        position_of_zero_in_given_puzzle = (1, 0)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [0, 4, 5], [6, 7, 8]]
        position_of_zero_in_final_state = (1, 0)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 0
        #list of reversed directions
        expected_directions = []

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_4_x_4_solved_puzzle_and_not_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 11], [12, 13, 14, 15]]
        position_of_zero_in_given_puzzle = (2, 1)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board =[[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 11], [12, 13, 14, 15]]
        position_of_zero_in_final_state = (2, 1)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 0
        #list of reversed directions
        expected_directions = []

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_given_5_x_5_solved_puzzle_and_not_last_position_of_zero_in_solved_puzzle(self):
        puzzle_board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 0, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        position_of_zero_in_given_puzzle = (2, 2)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 0, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        position_of_zero_in_final_state = (2, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 0
        #list of reversed directions
        expected_directions = []

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions)

    def test_with_first_example_from_presentations(self):
        puzzle_board = [[6, 5, 3], [2, 4, 8], [7, 0, 1]]
        position_of_zero_in_given_puzzle = (2, 1)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        position_of_zero_in_final_state = (2, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 21
        #list of reversed directions
        expected_directions = ['left', 'down', 'down', 'right', 'right', 'up', 'left', 'up',
                               'right', 'down', 'left', 'down', 'left', 'up', 'right', 'down',
                               'right', 'up', 'up', 'left', 'left']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions[::-1])

    def test_with_second_example_from_presentations(self):
        puzzle_board = [[2, 3, 6], [1, 5, 8], [4, 7, 0]]
        position_of_zero_in_given_puzzle = (2, 2)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        position_of_zero_in_final_state = (2, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 8
        #list of reversed directions
        expected_directions = ['down', 'down', 'right', 'right', 'up', 'up', 'left', 'left']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions[::-1])

    def test_with_third_example_from_presentations(self):
        puzzle_board = [[8, 6, 7], [2, 5, 4], [3, 0, 1]]
        position_of_zero_in_given_puzzle = (2, 1)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        position_of_zero_in_final_state = (2, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 31
        #list of reversed directions
        expected_directions = ['left', 'down', 'down', 'right', 'right', 'up', 'up', 'left',
                               'left', 'down', 'down', 'right', 'up', 'right', 'up', 'left', 'left', 'down', 'right', 'down',
                               'left', 'up', 'right', 'down', 'right', 'up', 'up', 'left', 'down', 'left', 'up']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions[::-1])

    def test_with_fourth_example_from_presentations(self):
        puzzle_board = [[6, 4, 7], [8, 5, 0], [3, 2, 1]]
        position_of_zero_in_given_puzzle = (1, 2)
        position_of_zero_in_solved_puzzle = -1
        puzzle = Puzzle_node(puzzle_board, position_of_zero_in_given_puzzle)
        final_state_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        position_of_zero_in_final_state = (2, 2)
        final_state = Puzzle_node(final_state_board, position_of_zero_in_final_state)

        steps, directions = iterative_deepening_a_star(puzzle, final_state, final_state.tile_number_position_dict)

        expected_steps = 31
        #list of reversed directions
        expected_directions = ['up', 'right', 'right', 'down', 'down',
                               'left', 'left', 'up', 'up', 'right', 'right',
                               'down', 'left', 'down', 'left', 'up', 'up', 'right',
                               'right', 'down', 'left', 'up', 'right', 'down', 'down',
                               'left', 'left', 'up', 'right', 'up', 'left']

        self.assertEqual(steps, expected_steps)
        self.assertEqual(directions, expected_directions[::-1])
