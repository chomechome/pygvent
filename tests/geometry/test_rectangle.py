import unittest

from pygvent.geometry import Point, Rectangle


class RectangleTest(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(1, 1, width=3, height=4)

    def test_equality(self):
        other = Rectangle(1, 1, width=3, height=4)
        self.assertEqual(other, self.rectangle)

    def test_inequality(self):
        for other in [
            Rectangle(1, 2, width=3, height=4),
            Rectangle(1, 1, width=2, height=4),
            Rectangle(1, 1, width=3, height=3),
            Rectangle(1, 1, width=2, height=2),
        ]:
            with self.subTest(other=other):
                self.assertNotEqual(other, self.rectangle)

    def test_from_coordinates(self):
        rectangle = Rectangle.from_coordinates(1, 1, 3, 4)
        self.assertEqual(Rectangle(1, 1, width=2, height=3), rectangle)

    def test_from_points(self):
        rectangle = Rectangle.from_points(Point(1, 1), Point(2, 3))
        self.assertEqual(Rectangle(1, 1, width=1, height=2), rectangle)

    def test_top(self):
        self.assertEqual(5, self.rectangle.top)

    def test_right(self):
        self.assertEqual(4, self.rectangle.right)

    def test_area(self):
        self.assertEqual(12, self.rectangle.area)

    def test_boolean(self):
        position = 0, 0
        self.assertTrue(Rectangle(*position, width=1, height=1))
        self.assertFalse(Rectangle(*position, width=0, height=1))
        self.assertFalse(Rectangle(*position, width=1, height=0))
        self.assertFalse(Rectangle(*position, width=0, height=0))

    def test_has_intersection(self):
        for other in [
            Rectangle(0, 0, width=2, height=2),
            Rectangle(0, 2, width=2, height=2),
            Rectangle(0, 4, width=2, height=2),
            Rectangle(2, 4, width=1, height=2),
            Rectangle(3, 4, width=2, height=2),
            Rectangle(3, 2, width=2, height=2),
            Rectangle(3, 0, width=2, height=2),
            Rectangle(2, 0, width=1, height=2),
        ]:
            with self.subTest(other=other):
                self.assertTrue(self.rectangle.intersects(other))

    def test_no_intersection(self):
        for other in [
            Rectangle(-1, -1, width=2, height=2),
            Rectangle(-1, 1, width=2, height=2),
            Rectangle(-1, 3, width=2, height=2),
            Rectangle(2, 5, width=1, height=2),
            Rectangle(3, 5, width=2, height=2),
            Rectangle(4, 2, width=2, height=2),
            Rectangle(4, 0, width=2, height=2),
            Rectangle(2, -1, width=1, height=2),
        ]:
            with self.subTest(other=other):
                self.assertFalse(self.rectangle.intersects(other))

    def test_intersection(self):
        for other, expected in [
            (Rectangle(0, 0, 2, 2), Rectangle(1, 1, 1, 1)),
            (Rectangle(0, 2, 2, 2), Rectangle(1, 2, 1, 2)),
            (Rectangle(0, 4, 2, 2), Rectangle(1, 4, 1, 1)),
            (Rectangle(2, 4, 1, 2), Rectangle(2, 4, 1, 1)),
            (Rectangle(3, 4, 2, 2), Rectangle(3, 4, 1, 1)),
            (Rectangle(3, 2, 2, 2), Rectangle(3, 2, 1, 2)),
            (Rectangle(3, 0, 2, 2), Rectangle(3, 1, 1, 1)),
            (Rectangle(2, 0, 1, 2), Rectangle(2, 1, 1, 1)),
            (Rectangle(-1, -1, 2, 2), None),
            (Rectangle(-1, 1, 2, 2), None),
            (Rectangle(-1, 3, 2, 2), None),
            (Rectangle(2, 5, 1, 2), None),
            (Rectangle(3, 5, 2, 2), None),
            (Rectangle(4, 2, 2, 2), None),
            (Rectangle(4, 0, 2, 2), None),
            (Rectangle(2, -1, 1, 2), None),
        ]:
            with self.subTest(other=other, expected=expected):
                self.assertEqual(expected, self.rectangle.intersect(other))
