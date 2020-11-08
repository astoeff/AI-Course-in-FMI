from math import sqrt

class Puzzle_node():
    def __init__(self, content, zero_position, distance_from_root = 0, father_node = None, movement_direction = None):
        self.content = content
        self.zero_position = zero_position
        self.distance_from_root = distance_from_root
        self.father_node = father_node
        self.children = None
        self.movement_direction = movement_direction

    def calculate_manhattan_distance(self, final_state_dict_values):
        lst_values_of_self = list(self.tile_number_position_dict.values())
        lst_values_of_final_state = list(final_state_dict_values.values())
        return  sum([abs(lst_values_of_self[i][0] - lst_values_of_final_state[i][0])\
                    + abs(lst_values_of_self[i][1] - lst_values_of_final_state[i][1]) for i in range(1, self.size * self.size)])

    def calculate_heuristic(self, final_state_dict_values):
        return self.distance_from_root + self.calculate_manhattan_distance(final_state_dict_values)

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
    