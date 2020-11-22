import unittest

from dot import Dot
from route import Route
from main import crossover

class TestCrossover(unittest.TestCase):
    def test_with_given_two_route_parents_with_even_number_of_genes_should_crossover_correctly(self):
        #ASSET
        #Route 1
        n = 4
        coordinates_for_dot_1_of_route_1 = (0, 2)
        coordinates_for_dot_2_of_route_1 = (2, 1)
        coordinates_for_dot_3_of_route_1 = (2, 2)
        coordinates_for_dot_4_of_route_1 = (1, 1)
        dot_1_of_route_1 = Dot(coordinates_for_dot_1_of_route_1)
        dot_2_of_route_1 = Dot(coordinates_for_dot_2_of_route_1)
        dot_3_of_route_1 = Dot(coordinates_for_dot_3_of_route_1)
        dot_4_of_route_1 = Dot(coordinates_for_dot_4_of_route_1)
        dots_route_1 = [dot_1_of_route_1, dot_2_of_route_1, dot_3_of_route_1, dot_4_of_route_1]
        route_1 = Route(dots_route_1)

        #Route 2
        coordinates_for_dot_1_of_route_2 = (2, 2)
        coordinates_for_dot_2_of_route_2 = (0, 2)
        coordinates_for_dot_3_of_route_2 = (1, 1)
        coordinates_for_dot_4_of_route_2 = (2, 1)
        dot_1_of_route_2 = Dot(coordinates_for_dot_1_of_route_2)
        dot_2_of_route_2 = Dot(coordinates_for_dot_2_of_route_2)
        dot_3_of_route_2 = Dot(coordinates_for_dot_3_of_route_2)
        dot_4_of_route_2 = Dot(coordinates_for_dot_4_of_route_2)
        dots_route_2 = [dot_1_of_route_2, dot_2_of_route_2, dot_3_of_route_2, dot_4_of_route_2]
        route_2 = Route(dots_route_2)

        #expected_children
        child_1 = Route([(0, 2), (2, 1), (1, 1), (2, 2)])
        child_2 = Route([(2, 2), (0, 2), (1, 1), (2, 1)])
        expected_children = (child_1, child_2)
        

        #ACT
        result_children = crossover(route_1, route_2, n)

        #ASSERT
        self.assertEqual(result_children, expected_children)

    def test_with_given_two_route_parents_with_odd_number_of_genes_should_crossover_correctly(self):
        #ASSET
        #Route 1
        n = 3
        coordinates_for_dot_1_of_route_1 = (0, 2)
        coordinates_for_dot_2_of_route_1 = (2, 1)
        coordinates_for_dot_3_of_route_1 = (2, 2)
        dot_1_of_route_1 = Dot(coordinates_for_dot_1_of_route_1)
        dot_2_of_route_1 = Dot(coordinates_for_dot_2_of_route_1)
        dot_3_of_route_1 = Dot(coordinates_for_dot_3_of_route_1)
        dots_route_1 = [dot_1_of_route_1, dot_2_of_route_1, dot_3_of_route_1]
        route_1 = Route(dots_route_1)

        #Route 2
        coordinates_for_dot_1_of_route_2 = (2, 2)
        coordinates_for_dot_2_of_route_2 = (0, 2)
        coordinates_for_dot_3_of_route_2 = (2, 1)
        dot_1_of_route_2 = Dot(coordinates_for_dot_1_of_route_2)
        dot_2_of_route_2 = Dot(coordinates_for_dot_2_of_route_2)
        dot_3_of_route_2 = Dot(coordinates_for_dot_3_of_route_2)
        dots_route_2 = [dot_1_of_route_2, dot_2_of_route_2, dot_3_of_route_2]
        route_2 = Route(dots_route_2)

        #expected_children
        child_1 = Route([(0, 2), (2, 1), (2, 2)])
        child_2 = Route([(2, 2), (0, 2), (2, 1)])
        expected_children = (child_1, child_2)
        

        #ACT
        result_children = crossover(route_1, route_2, n)

        #ASSERT
        self.assertEqual(result_children, expected_children)
