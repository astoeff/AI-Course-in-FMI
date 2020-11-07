from math import sqrt

# from constants import SOLVED_PUZZLES_TILES_POSITIONS, FINAL_PUZZLE_STATES

class Puzzle_node():
    def __init__(self, content, zero_position, distance_from_root = 0, father_node = None, movement_direction = None):
        self.content = content
        self.zero_position = zero_position
        self.distance_from_root = distance_from_root
        self.father_node = father_node
        self.children = None
        self.movement_direction = movement_direction
        # self.final_state = final_state

    # @property
    # def manhattan_distance(self):
    #     manhattan_distance = 0
    #     tile_x = 0
    #     for row in self.content:
    #         tile_y = 0
    #         for tile in row:
    #             if tile != 0:
    #                 manhattan_distance += abs(tile_x - SOLVED_PUZZLES_TILES_POSITIONS[self.size][tile][0]) + abs(tile_y - SOLVED_PUZZLES_TILES_POSITIONS[self.size][tile][1])
    #             tile_y += 1
    #         tile_x += 1
    #     return manhattan_distance

    def calculate_manhattan_distance(self, final_state):
        return  sum([(abs((list(self.tile_number_position_dict.values()))[i][0] - (list(final_state.tile_number_position_dict.values()))[i][0])\
                    + abs((list(self.tile_number_position_dict.values()))[i][1] - (list(final_state.tile_number_position_dict.values()))[i][1])) for i in range(1, self.size * self.size)])

        # m = 0
        # vals1 = list(self.tile_number_position_dict.values())
        # vals2 = list(final_state.tile_number_position_dict.values())
        # print(vals1)
        # print(vals2)
        # for i in range(0, self.size*self.size):
        #    m += self.

    def calculate_heuristic(self, final_state):
        # print(self.calculate_manhattan_distance(final_state))
        return self.distance_from_root + self.calculate_manhattan_distance(final_state)

    @property
    def tile_number_position_dict(self):
        tile_number_position_dict = {}
        tile_x = 0
        for row in self.content:
            tile_y = 0
            for tile in row:
                tile_number_position_dict[tile] = (tile_x, tile_y)
                tile_y += 1
            tile_x += 1
        return dict(sorted(tile_number_position_dict.items()))
    

    @property
    def size(self):
        return len(self.content[0])

    @property
    def is_solved(self):
        return self.content == FINAL_PUZZLE_STATES[self.size]

    @property
    def is_solvable(self):
        return True    

    def print_puzzle(self):
        for i in self.content:
            print(i)

    def __eq__(self, other): 
        if not isinstance(other, Puzzle_node):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.content == other.content
    