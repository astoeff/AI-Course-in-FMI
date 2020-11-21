class Route():
	def __init__(self, dots):
		self.dots = dots
		self.length = len(dots)

	@property
	def distance(self):
		return sum([self.dots[i].distance_to_dot(self.dots[i + 1]) for i in range(0, self.length - 1)])
	
	def print_dots(self):
		for dot in self.dots:
			dot.print_coordinates()