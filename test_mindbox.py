import unittest
import math
from mindbox import Circle, Triangle


class TestFigures(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 5 ** 2)

    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)

    def test_triangle_right_angled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angled())
