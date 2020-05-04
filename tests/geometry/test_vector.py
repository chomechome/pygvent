import math
import unittest

from pygvent.geometry import Vector, Point


class VectorTest(unittest.TestCase):
    def setUp(self):
        self.vector = Vector(1, 2)

    def test_iter(self):
        self.assertEqual([1, 2], [coordinate for coordinate in self.vector])

    def test_equality(self):
        self.assertEqual(Vector(1, 2), self.vector)

    def test_inequality(self):
        for other in [Point(1, 2), [1, 2], (1, 2), Vector(2, 2), Vector(2, 1)]:
            with self.subTest(other=other):
                self.assertNotEqual(other, self.vector)

    def test_zeros(self):
        self.assertEqual(Vector(0, 0), Vector.zeros())

    def test_ones(self):
        self.assertEqual(Vector(1, 1), Vector.ones())

    def test_boolean(self):
        self.assertTrue(Vector(1, 1))
        self.assertTrue(Vector(1, 0))
        self.assertTrue(Vector(0, 1))
        self.assertFalse(Vector(0, 0))

    def test_copy(self):
        copy = self.vector.copy()
        self.assertEqual(self.vector, copy)
        self.assertIsNot(self.vector, copy)

    def test_addition(self):
        self.assertEqual(Vector(4, 6), self.vector + Vector(3, 4))

    def test_addition_inplace(self):
        self.vector += Vector(2, 1)
        self.assertEqual(Vector(3, 3), self.vector)

    def test_subtraction(self):
        self.assertEqual(Vector(-2, -2), self.vector - Vector(3, 4))

    def test_subtraction_inplace(self):
        self.vector -= Vector(2, 1)
        self.assertEqual(Vector(-1, 1), self.vector)

    def test_multiplication(self):
        self.assertEqual(Vector(2, 4), self.vector * 2)

    def test_right_operand_multiplication(self):
        self.assertEqual(Vector(3, 6), 3 * self.vector)

    def test_multiplication_inplace(self):
        self.vector *= 3
        self.assertEqual(Vector(3, 6), self.vector)

    def test_division(self):
        factor = 2
        expected = Vector(0.5, 1.0)

        self.assertEqual(expected, self.vector / factor)

    def test_division_inplace(self):
        factor = 4
        expected = Vector(0.25, 0.5)

        self.vector /= factor
        self.assertEqual(expected, self.vector)

    def test_negative(self):
        self.assertEqual(Vector(-1, -2), -self.vector)

    def test_absolute(self):
        self.assertEqual(Vector(3, 2), abs(Vector(-3, -2)))

    def test_length(self):
        self.assertEqual(math.sqrt(5), self.vector.length)

    def test_squared_length(self):
        self.assertEqual(5, self.vector.squared_length)

    def test_zero_angle(self):
        self.assertEqual(0, Vector(10, 0).angle)

    def test_right_angle(self):
        self.assertEqual(90, Vector(0, 10).angle)

    def test_set_angle(self):
        self.vector.angle = 45
        self.assertEqual(45, self.vector.angle)

    def test_rotate_clockwise(self):
        self.assertAlmostEqual(90, Vector(1, 0).rotate(90).angle)

    def test_rotate_counterclockwise(self):
        self.assertAlmostEqual(0, Vector(0, 1).rotate(-90).angle)

    def test_rotate_inplace(self):
        vector = Vector(1, 1)

        vector.rotate(-90, inplace=True)
        self.assertAlmostEqual(-45, vector.angle)

    def test_get_angle_between(self):
        vector = Vector(1, 1)
        other = Vector(0, 1)

        self.assertAlmostEqual(45, vector.get_angle(other))
        self.assertAlmostEqual(-45, other.get_angle(vector))

    def test_perpendicular(self):
        perpendicular = self.vector.perpendicular

        self.assertEqual(90, self.vector.get_angle(perpendicular))

    def test_normalize(self):
        expected = Vector(1 / self.vector.length, 2 / self.vector.length)
        self.assertEqual(expected, self.vector.normalized)

    def test_normalize_zero_vector(self):
        self.assertEqual(Vector(0, 0), Vector.zeros().normalized)

    def test_dot_product(self):
        self.assertEqual(12, Vector(2, 2).dot(Vector(1, 5)))

    def test_cross_product(self):
        self.assertEqual(-14, Vector(1, 5).cross(Vector(4, 6)))
