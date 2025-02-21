import unittest
from math import isclose

from .rectangle import area_rectangle, perimeter_rectangle
class RectangleTestCase(unittest.TestCase):

    def test_correct(self):
        test_area_data = [
            (2, 5, 10),
            (15, 2, 30),
            (6, 5, 30),
            (6, 60, 360)
        ]
        for width, height, expect in test_area_data:
            with self.subTest(width=width, height=height):
                self.assertEqual(area_rectangle(width, height), expect)

        test_perim_data = [
            (2, 2, 5, 5, 14),
            (2, 5, 2, 5, 14),
            (2, 5, 5, 2, 14),
            (2, 5, 2, 5, 14)
        ]
        for param_1, param_2, param_3, param_4, expect in test_perim_data:
            with self.subTest(param_1=param_1, param_2=param_2, param_3=param_3, param_4=param_4):
                self.assertEqual(perimeter_rectangle(param_1, param_2, param_3, param_4), expect)

    def test_accuracy_results(self):
        test_area_data = [
            (2.852, 5.432,15.492064),
            (15.345678980, 2.45784930,37.71736633901771),
            (6.000000004, 5.4387,32.6322000217548),
            (6.009, 6.991, 42.008919)
        ]
        for width, height, expect in test_area_data:
            with self.subTest(width=width, height=height):
                res = area_rectangle(width, height)
                self.assertTrue(isclose(res, expect))

        test_perim_data = [
            (15.492064, 5.4387, 15.492064, 5.4387, 41.861528),
            (6.000000004, 6.000000004, 6.000000004, 6.000000004, 24.000000016),
            (6.009, 6.009, 6.991, 6.991, 26),
            (42.008919, 37.71736633901771, 37.71736633901771, 42.008919, 159.45257067803542)
        ]
        for param_1, param_2, param_3, param_4, expect in test_perim_data:
            with self.subTest(param_1=param_1, param_2=param_2, param_3=param_3, param_4=param_4):
                res = perimeter_rectangle(param_1, param_2, param_3, param_4)
                self.assertTrue(isclose(res, expect))
    
from circle import area_circle, perimeter_circle
class CircleTestCase(unittest.TestCase):
    
    def test_correct(self):
        test_area_data = [
            (5, 78.539816339744831),
            (134, 56410.43768785832739),
            (56, 9852.034561657591596),
            (2, 12.566370614359173)
        ]
        for radius, expect in test_area_data:
            with self.subTest(radius=radius):
                res = area_circle(radius)
                self.assertTrue(isclose(res, expect))

        test_perim_data = [
            (5, 31.415926535897932),
            (134, 841.946831162064588),
            (56, 351.858377202056843),
            (2, 12.566370614359173)
        ]
        for radius, expect in test_perim_data:
            with self.subTest(radius=radius):
                res = perimeter_circle(radius)
                self.assertTrue(isclose(res, expect))

from square import area_square, perimeter_square
class SquareTestCase(unittest.TestCase):
    def test_correct(self):
        test_area_data = [
            (5, 25),
            (134, 17956),
            (56, 3136),
            (2, 4)
        ]
        for side, expect in test_area_data:
            with self.subTest(side=side):
                self.assertEqual(expect, area_square(side))

        test_perim_data = [
            (5, 20),
            (134, 536),
            (56, 224),
            (2, 8)
        ]
        for side, expect in test_perim_data:
            with self.subTest(side=side):
                self.assertEqual(expect, perimeter_square(side))

    def test_accuracy_results(self):
        test_area_data = [
            (37.71736633901771, 1422.599723551666212),
            (159.45257067803542, 25425.122295833874622),
            (32.6322000217548, 1064.86047825981397),
            (42.008919, 1764.749275548561)
        ]
        for side, expect in test_area_data:
            with self.subTest(side=side):
                self.assertTrue(isclose(expect, area_square(side)))

        test_perim_data = [
            (37.71736633901771, 150.86946535607084),
            (159.45257067803542, 637.8102827121416),
            (32.6322000217548, 130.5288000870192),
            (42.008919, 168.035676)
        ]
        for side, expect in test_perim_data:
            with self.subTest(side=side):
                self.assertTrue(isclose(expect, perimeter_square(side)))


from triangle import area_triangle, perimeter_triangle
class TriangleTestCase(unittest.TestCase):

    def test_correct(self):
        test_area_data = [
            (4, 5, 10),
            (30, 2, 30),
            (6, 8, 24),
            (10, 7, 35)
        ]
        for osn, height, expect in test_area_data:
            with self.subTest(osn=osn, height=height):
                self.assertEqual(area_triangle(osn, height), expect)

        test_perim_data = [
            (2, 8, 6, 16),
            (4, 5, 6, 15),
            (19, 4, 20, 43),
            (8, 18, 23, 49)
        ]
        for param_1, param_2, param_3, expect in test_perim_data:
            with self.subTest(param_1=param_1, param_2=param_2, param_3=param_3):
                self.assertEqual(perimeter_triangle(param_1, param_2, param_3), expect)

    def test_accuracy_results(self):
        test_area_data = [
            (2.852, 5.432, 7.746032),
            (15.345678980, 2.45784930, 18.858683169508855),
            (6.000000004, 5.4387, 16.3161000108774),
            (6.009, 6.991, 21.0044595)
        ]
        for osn, height, expect in test_area_data:
            with self.subTest(osn=osn, height=height):
                res = area_triangle(osn, height)
                self.assertTrue(isclose(res, expect))

        test_perim_data = [
            (15.492064, 5.4387, 11.492064, 32.422828),
            (6.000000004, 3.000000004, 5.000000004, 14.000000012),
            (42.008919, 37.71736633901771, 32.008919, 111.73520433901771)
        ]
        for param_1, param_2, param_3, expect in test_perim_data:
            with self.subTest(param_1=param_1, param_2=param_2, param_3=param_3):
                res = perimeter_triangle(param_1, param_2, param_3)
                self.assertTrue(isclose(res, expect))
