from math import sqrt

from constants import SOLVED_PUZZLE_TILES_POSITIONS_DICT

class Puzzle_node():
    def __init__(self, content, zero_position, distance_from_root = 0, father_node = None):
        self.content = content
        self.zero_position = zero_position
        self.distance_from_root = distance_from_root
        self.father_node = father_node

    @property
    def manhattan_distance(self):
        manhattan_distance = 0
        tile_x = 0
        for row in self.content:
            tile_y = 0
            for tile in row:
                if tile != 0:
                    manhattan_distance += abs(tile_x - SOLVED_PUZZLE_TILES_POSITIONS_DICT[tile][0]) + abs(tile_y - SOLVED_PUZZLE_TILES_POSITIONS_DICT[tile][1])
                tile_y += 1
            tile_x += 1
        return manhattan_distance

    @property
    def heuristic(self):
        return self.distance_from_root + self.manhattan_distance

    @property
    def is_solved(self):
        return False

    @property
    def is_solvable(self):
        return True

    @property
    def children(self):
        return True
    

    def print_puzzle(self):
        for i in self.content:
            print(i)
    