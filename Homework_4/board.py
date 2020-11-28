from constants import UPPER_LABEL_OF_PRINTING_BOARD_STRING


class Board():
	def __init__(self, board):
		self.board = board

	def update(self, position, sign):
		self.board[position[0]][position[1]] = sign

	def check_if_solved_by_row(self):
		solved_with_sign = '_'
		for row in self.board:
			if row[0] == row[1] == row[2] and row[0] != '_':
				solved_with_sign = row[0]
				break
		return solved_with_sign

	def print(self):
		print(UPPER_LABEL_OF_PRINTING_BOARD_STRING)
		count = 0
		for row in self.board:
			print(str(count) + ' ' + " ".join(row))
			count += 1