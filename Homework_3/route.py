from dot import Dot

class Route():
	def __init__(self, dots):
		for dot in dots:
			assert type(dot) == Dot, 'Dots must be of type [<Dot>] not [<tuple>]'
		self.dots = dots
		self.length = len(dots)

	@property
	def distance(self):
		return sum([self.dots[i].distance_to_dot(self.dots[i + 1]) for i in range(0, self.length - 1)])
	
	def print_dots(self):
		for dot in self.dots:
			dot.print_coordinates()

	def __lt__(self, other):
		return self.distance < other.distance

	def __eq__(self, other):
		return self.dots == other.dots

	def __str__(self):
		return str(self.dots)