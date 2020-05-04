import unittest

from pygvent.geometry import Point, Vector


class PointTest(unittest.TestCase):
    def setUp(self):
        self.point = Point(1, 2)

    def test_iter(self):
        self.assertEqual([1, 2], [coordinate for coordinate in self.point])

    def test_equality(self):
        self.assertEqual(Point(1, 2), self.point)

    def test_inequality(self):
        for other in [
            Vector(1, 2),
            [1, 2],
            (1, 2),
            Point(2, 2),
            Point(2, 1),
        ]:
            with self.subTest(other=other):
                self.assertNotEqual(other, self.point)

    def test_zeros(self):
        self.assertEqual(Point(0, 0), Point.zeros())

    def test_ones(self):
        self.assertEqual(Point(1, 1), Point.ones())

    def test_boolean(self):
        self.assertTrue(Point(1, 1))
        self.assertTrue(Point(1, 0))
        self.assertTrue(Vector(0, 1))
        self.assertFalse(Vector(0, 0))

    def test_copy(self):
        copy = self.point.copy()
        self.assertEqual(self.point, copy)
        self.assertIsNot(self.point, copy)

    def test_addition(self):
        self.assertEqual(Point(3, 4), self.point + Vector(2, 2))

    def test_subtraction(self):
        self.assertEqual(Vector(-1, 2), Point(0, 4) - self.point)

    def test_right_operand_subtraction(self):
        self.assertEqual(Vector(1, -2), self.point - Point(0, 4))

    def test_negative(self):
        self.assertEqual(Point(-1, -2), -self.point)

    def test_absolute(self):
        self.assertEqual(Point(3, 2), abs(Point(-3, -2)))

    def test_distance(self):
        self.assertEqual(5, self.point.get_distance(Point(4, 6)))
