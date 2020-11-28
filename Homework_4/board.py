from constants import UPPER_LABEL_OF_PRINTING_BOARD_STRING


class Board():
	def __init__(self, board):
		self.board = board

	def print(self):
		print(UPPER_LABEL_OF_PRINTING_BOARD_STRING)
		count = 0
		for row in self.board:
			print(str(count) + ' ' + " ".join(row))
			count += 1