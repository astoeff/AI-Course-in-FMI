from math import sqrt

class Dot():
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.x = coordinates[0]
        self.y = coordinates[1]

    def distance_to_dot(self, other):
        return round(sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2)), 2)

    def print_coordinates(self):
        print(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __str__(self):
        return str(self.coordinates)
