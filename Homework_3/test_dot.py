import unittest

from dot import Dot
# from decimal import *

class TestDistanceToDot(unittest.TestCase):
    def test_with_given_non_different_dots_should_return_zero(self):
        #ASSET
        coordinates = (0, 0)
        dot_1 = Dot(coordinates)
        dot_2 = Dot(coordinates)
        expected_distance = 0

        #ACT
        result_distance = dot_1.distance_to_dot(dot_2)

        #ASSERT
        self.assertEqual(result_distance, expected_distance)

    def test_with_given_different_dots_should_return_correct_distance(self):
        #ASSET
        coordinates_for_dot_1 = (0, 1)
        coordinates_for_dot_2 = (2, 0)
        dot_1 = Dot(coordinates_for_dot_1)
        dot_2 = Dot(coordinates_for_dot_2)
        expected_distance = 2.24

        #ACT
        result_distance = dot_1.distance_to_dot(dot_2)

        #ASSERT
        self.assertEqual(result_distance, expected_distance)