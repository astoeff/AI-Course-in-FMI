from termcolor import colored

from constants import UPPER_LABEL_OF_PRINTING_BOARD_STRING, EMPTY_POSITION_ON_BOARD_CHAR, BOARD_FINAL_STATE_CHAR


class Board():
    def __init__(self, board):
        self.board = board
        self.solved_sign = EMPTY_POSITION_ON_BOARD_CHAR

    def update(self, position, sign):
        self.board[position[0]][position[1]] = sign

    def check_if_solved_by_row(self):
        solved_with_sign = EMPTY_POSITION_ON_BOARD_CHAR
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != EMPTY_POSITION_ON_BOARD_CHAR:
                solved_with_sign = row[0]
                break
        return solved_with_sign

    def check_if_solved_by_col(self):
        solved_with_sign = EMPTY_POSITION_ON_BOARD_CHAR
        if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != EMPTY_POSITION_ON_BOARD_CHAR:
            solved_with_sign = self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != EMPTY_POSITION_ON_BOARD_CHAR:
            solved_with_sign = self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != EMPTY_POSITION_ON_BOARD_CHAR:
            solved_with_sign = self.board[0][2]
        return solved_with_sign

    def check_if_solved_by_diagonals(self):
        solved_with_sign = EMPTY_POSITION_ON_BOARD_CHAR
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != EMPTY_POSITION_ON_BOARD_CHAR:
            solved_with_sign = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != EMPTY_POSITION_ON_BOARD_CHAR:
            solved_with_sign = self.board[0][2]
        return solved_with_sign

    def check_if_solved(self):
        sign_for_solved_by_row = self.check_if_solved_by_row()
        sign_for_solved_by_col = self.check_if_solved_by_col()
        sign_for_solved_by_diagonals = self.check_if_solved_by_diagonals()
        board_solved_with_sign = EMPTY_POSITION_ON_BOARD_CHAR
        if sign_for_solved_by_row != EMPTY_POSITION_ON_BOARD_CHAR:
            board_solved_with_sign = sign_for_solved_by_row
        elif sign_for_solved_by_col != EMPTY_POSITION_ON_BOARD_CHAR:
            board_solved_with_sign = sign_for_solved_by_col
        elif sign_for_solved_by_diagonals != EMPTY_POSITION_ON_BOARD_CHAR:
            board_solved_with_sign = sign_for_solved_by_diagonals
        self.solved_sign = board_solved_with_sign
        return board_solved_with_sign

    def check_if_final_state(self):
        board_solved_with_sign = self.check_if_solved()
        if board_solved_with_sign == EMPTY_POSITION_ON_BOARD_CHAR:
            for i in range(0, 3):
                for j in range(0, 3):
                    # There's an empty field, we continue the game
                    if (self.board[i][j] == EMPTY_POSITION_ON_BOARD_CHAR):
                        self.solved_sign = EMPTY_POSITION_ON_BOARD_CHAR
                        return EMPTY_POSITION_ON_BOARD_CHAR
            self.solved_sign = BOARD_FINAL_STATE_CHAR
            return BOARD_FINAL_STATE_CHAR
        else:
            self.solved_sign = board_solved_with_sign
            return board_solved_with_sign

    def print(self):
        print(UPPER_LABEL_OF_PRINTING_BOARD_STRING)
        count = 0
        for row in self.board:
            print(str(count) + ' ' + " ".join(row))
            count += 1

    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.board[0][i] != '_' and
                self.board[0][i] == self.board[1][i] and
                self.board[1][i] == self.board[2][i]):
                return self.board[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.board[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.board[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.board[0][0] != '_' and
            self.board[0][0] == self.board[1][1] and
            self.board[0][0] == self.board[2][2]):
            return self.board[0][0]

        # Second diagonal win
        if (self.board[0][2] != '_' and
            self.board[0][2] == self.board[1][1] and
            self.board[0][2] == self.board[2][0]):
            return self.board[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.board[i][j] == '_'):
                    return None

        # It's a tie!
        return '_'