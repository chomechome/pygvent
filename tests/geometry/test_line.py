import unittest

from broadway.geometry import Point, Vector, Line


class LineTest(unittest.TestCase):
    def setUp(self):
        self.line = Line(Point(-2, -1), Vector(4, 2))

    def test_initialize_with_zero_direction(self):
        with self.assertRaises(AssertionError):
            Line(Point.zeros(), Vector.zeros())

    def test_set_zero_direction(self):
        with self.assertRaises(AssertionError):
            self.line.direction = Vector.zeros()

    def test_equality(self):
        for other in [
            Line(Point(-2, -1), Vector(2, 1)),
            Line(Point(0, 0), Vector(4, 2)),
        ]:
            with self.subTest(other=other):
                self.assertEqual(other, self.line)

    def test_inequality(self):
        for other in [
            Line(Point(1, 0), Vector(4, 2)),
            Line(Point(-2, -1), Vector(3, 2)),
        ]:
            with self.subTest(other=other):
                self.assertNotEqual(other, self.line)

    def test_contains(self):
        for item in [
            Vector(-2, -1),
            Point(0, 0),
            Point(2, 1),
            Vector(4, 2),
            Point(6, 3),
        ]:
            with self.subTest(item=item):
                self.assertIn(item, self.line)

    def test_does_not_contain(self):
        for item in [
            Vector(-3, -1),
            Point(1, 0),
            Point(0, 1),
            Vector(4, 2.01),
            Point(0.01, 0),
            Point(0, 0.01),
            1,
            (2, 1),
            [0, 0],
        ]:
            with self.subTest(item=item):
                self.assertNotIn(item, self.line)

    def test_from_points(self):
        new_line = Line.from_points(Point(1, 0), Point(3, 2))
        self.assertEqual(Line(Point(1, 0), Vector(2, 2)), new_line)
