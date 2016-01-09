import unittest
import pickle
from pygvent.vector2d import Vector2D, VectorIndexError, VectorArgumentError


class Vector2DTest(unittest.TestCase):
    def setUp(self):
        self.vector = Vector2D(111., 222.)

    def test_access(self):
        self.assertTrue(self.vector.x == 111 and self.vector.y == 222)
        self.assertTrue(self.vector[0] == 111 and self.vector[1] == 222)

        self.assertRaises(VectorIndexError, self.vector.__getitem__,
                          key=len(self.vector) + 100)

    def test_set(self):
        self.vector.x = 333
        self.assertTrue(self.vector.x == 333 and self.vector[0] == 333)

        self.vector[1] = 444
        self.assertTrue(self.vector.y == 444 and self.vector[1] == 444)

        self.assertRaises(VectorIndexError, self.vector.__setitem__,
                          key=len(self.vector) + 100, value=999)

    def test_equality(self):
        equals = [Vector2D(111, 222), (111, 222), [111, 222],
                  Vector2D(111., 222.), (111., 222.), [111., 222.]]
        for other in equals:
            self.assertEqual(self.vector, other)

        non_equals = [Vector2D(112, 222), (111, 223), [110, 222],
                      Vector2D(0., 0), 5, False, [3, -2, -5], [0, 0]]
        for other in non_equals:
            self.assertNotEqual(self.vector, other)

    def test_left_operand_math(self):
        self.assertEqual(self.vector + 1, Vector2D(112, 223))
        self.assertEqual(self.vector - 2, [109, 220])
        self.assertEqual(self.vector * 3, (333, 666))
        self.assertEqual(self.vector / 2.0, Vector2D(55.5, 111))
        self.assertEqual(self.vector / 2, (55.5, 111))
        self.assertEqual(self.vector ** Vector2D(2, 3), [12321, 10941048])
        self.assertEqual(self.vector + [-11, 78], Vector2D(100, 300))
        self.assertEqual(self.vector / [10, 2], [11.1, 111])

        self.assertRaises(VectorArgumentError, self.vector.__add__,
                          other=[123, 123, 123])
        self.assertRaises(VectorArgumentError, self.vector.__mul__,
                          other=(1, 3, 4, 5))

    def test_right_operand_math(self):
        self.assertEqual(1 + self.vector, Vector2D(112, 223))
        self.assertEqual(2 - self.vector, [-109, -220])
        self.assertEqual(3 * self.vector, (333, 666))
        self.assertEqual([222, 888] / self.vector, [2, 4])
        self.assertEqual([111, 222] ** Vector2D(2, 3), [12321, 10941048])
        self.assertEqual([-11, 78] + self.vector, Vector2D(100, 300))

        self.assertRaises(VectorArgumentError, self.vector.__radd__,
                          other=(4, 123123123, 1))
        self.assertRaises(VectorArgumentError, self.vector.__rmul__,
                          other=range(100))

    def test_inplace_math(self):
        reference = self.vector

        self.vector *= .5
        self.vector += .5
        self.vector /= (3, 6)
        self.vector += Vector2D(-1, -1)
        self.assertEqual(self.vector, reference)

    def test_unary_math(self):
        self.vector = -self.vector
        self.assertEqual(self.vector, [-111, -222])
        self.assertEqual(abs(self.vector), [111, 222])

    def test_length(self):
        self.vector = Vector2D(3, 4)

        self.assertEqual(self.vector.length, 5)
        self.assertEqual(self.vector.squared_length, 25)

        self.vector.length = 10
        self.assertEqual(self.vector, Vector2D(6, 8))
        self.assertEqual(self.vector.length, 10)

    def test_distance(self):
        self.vector = Vector2D(3, 4)
        other = Vector2D(10, -2)

        self.assertEqual(self.vector.get_squared_distance(other), 85)
        self.assertEqual(self.vector.get_distance(other),
                         (self.vector - other).length)

    def test_angles(self):
        self.vector = Vector2D(0, 3)
        self.assertEquals(self.vector.angle, 90)

        rotated = self.vector.rotate(-90)
        self.assertAlmostEqual(rotated.angle, 0)
        self.assertEqual(rotated.get_angle_between(self.vector), 90)
        self.assertEqual(self.vector.get_angle_between(rotated), -90)

        self.vector.angle -= 90
        self.assertEqual(self.vector.length, rotated.length)
        self.assertEqual(self.vector.angle, 0)
        self.assertEqual(self.vector, [3, 0])

        rotated.rotate(300, inplace=True)
        self.assertAlmostEqual(self.vector.get_angle_between(rotated), -60)
        rotated.rotate(rotated.get_angle_between(self.vector), inplace=True)
        self.assertAlmostEqual(self.vector.get_angle_between(rotated), 0)

        self.vector.angle = 90
        self.assertEqual(self.vector.angle, 90)
        self.assertEqual(round(self.vector, 15), [0, 3])

    def test_basis_vectors(self):
        self.vector = Vector2D(10, 1)
        x_base = Vector2D(5., 0)
        y_base = Vector2D(0, .5)

        self.assertEqual(self.vector.convert_to_basis(x_base, y_base), [2, 2])
        self.assertEqual(self.vector.project(x_base), (10, 0))
        self.assertEqual(x_base.dot(y_base), 0)

    def test_cross(self):
        lhs = Vector2D(1, .5)
        rhs = Vector2D(4, 6)
        self.assertEqual(lhs.cross(rhs), 4)

    def test_serialization(self):
        serialized = pickle.dumps(self.vector)
        deserialized = pickle.loads(serialized)
        self.assertEquals(self.vector, deserialized)

    def test_convert(self):
        self.assertIsInstance(Vector2D.convert((1, 2)), Vector2D)
        self.assertIsInstance(Vector2D.convert([1, 2]), Vector2D)
        self.assertIs(Vector2D.convert(self.vector), self.vector)

        self.assertRaises(TypeError, Vector2D.convert, (1, 2, 3))
        self.assertRaises(TypeError, Vector2D.convert, [1, 2, 3])
