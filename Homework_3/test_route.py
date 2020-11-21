import unittest

from dot import Dot
from route import Route

class TestDistance(unittest.TestCase):
    def test_with_given_route_should_return_correct_distance(self):
        #ASSET
        coordinates_for_dot_1 = (0, 2)
        coordinates_for_dot_2 = (2, 1)
        coordinates_for_dot_3 = (2, 2)
        dot_1 = Dot(coordinates_for_dot_1)
        dot_2 = Dot(coordinates_for_dot_2)
        dot_3 = Dot(coordinates_for_dot_3)
        dots = [dot_1, dot_2, dot_3]
        route = Route(dots)
        expected_distance = 3.24

        #ACT
        result_distance = route.distance

        #ASSERT
        self.assertEqual(result_distance, expected_distance)
