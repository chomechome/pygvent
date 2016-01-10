import math
import operator
from pygvent.utils import is_subscriptable


class VectorIndexError(IndexError):
    def __init__(self, obj, key):
        msg = "'{}' has length {}, got key {}".format(type(obj).__name__,
                                                      len(obj), key)
        super(VectorIndexError, self).__init__(msg)


class VectorArgumentError(TypeError):
    def __init__(self, obj, other):
        msg = "'{}' only accepts subscriptable arguments of length {}, got " \
              "'{}' with length {}".format(type(obj).__name__, len(obj),
                                           type(other).__name__, len(other))
        super(VectorArgumentError, self).__init__(msg)


class Vector2D(object):
    """
    2d vector, supports vector and scalar operators
    """

    __slots__ = ('x', 'y',)

    def __init__(self, x, y):
        """

        :type x: int|float
        :type y: int|float
        """
        self.x = x
        self.y = y

    @property
    def squared_length(self):
        return self.x ** 2 + self.y ** 2

    @property
    def length(self):
        return math.sqrt(self.squared_length)

    @length.setter
    def length(self, value):
        length = self.length
        self.x *= value / length
        self.y *= value / length

    @property
    def angle(self):
        if self.squared_length == 0:
            return 0
        return math.degrees(math.atan2(self.y, self.x))

    @angle.setter
    def angle(self, angle):
        self.x = self.length
        self.y = 0
        self.rotate(angle, inplace=True)

    def rotate(self, angle, inplace=False):
        """

        :param int|float angle: Angle in degrees
        :param bool inplace: If True, method changes current instance
        :rtype: Vector2D
        """
        radians = math.radians(angle)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos

        if not inplace:
            return Vector2D(x, y)

        self.x = x
        self.y = y
        return self

    @classmethod
    def convert(cls, iterable):
        if isinstance(iterable, cls):
            return iterable
        return cls(*iterable)

    @classmethod
    def zeros(cls):
        return cls(0, 0)

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        raise VectorIndexError(self, key)

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise VectorIndexError(self, key)

    def __repr__(self):
        return '{}({}, {})'.format(type(self).__name__, self.x, self.y)

    def __eq__(self, other):
        if is_subscriptable(other) and len(other) == len(self):
            return self.x == other[0] and self.y == other[1]
        return False

    def __ne__(self, other):
        return not self == other

    def __nonzero__(self):
        return bool(self.x or self.y)

    def copy(self):
        return Vector2D(self.x, self.y)

    def _is_valid_subscriptable(self, other):
        if is_subscriptable(other):
            if len(other) != len(self):
                raise VectorArgumentError(self, other)
            return True
        return False

    def _handle_left_operand_function(self, other, function):
        """
        Handles any two-operator function where the left operand is a Vector2D
        :type other: Vector2D|list|tuple|int|float
        :param callable function: Function to implement
        :rtype: Vector2D
        """
        if self._is_valid_subscriptable(other):
            return Vector2D(function(self.x, other[0]),
                            function(self.y, other[1]))
        return Vector2D(function(self.x, other), function(self.y, other))

    def _handle_right_operand_function(self, other, function):
        """
        Handles any two-operator function where the right operand is a Vector2D
        :type other: Vector2D|list|tuple|int|float
        :param callable function: Function to implement
        :rtype: Vector2D
        """
        if self._is_valid_subscriptable(other):
            return Vector2D(function(other[0], self.x),
                            function(other[1], self.y))
        return Vector2D(function(other, self.x), function(other, self.y))

    def _handle_function_inplace(self, other, function):
        """
        Handles any two-operator function inplace
        :type other: Vector2D|list|tuple|int|float
        :param callable function: Function to implement
        :rtype: Vector2D
        """
        if self._is_valid_subscriptable(other):
            self.x = function(self.x, other[0])
            self.y = function(self.y, other[1])
        else:
            self.x = function(self.x, other)
            self.y = function(self.y, other)
        return self

    def __add__(self, other):
        return self._handle_left_operand_function(other, operator.add)

    def __radd__(self, other):
        return self._handle_right_operand_function(other, operator.add)

    def __iadd__(self, other):
        return self._handle_function_inplace(other, operator.add)

    def __sub__(self, other):
        return self._handle_left_operand_function(other, operator.sub)

    def __rsub__(self, other):
        return self._handle_right_operand_function(other, operator.sub)

    def __isub__(self, other):
        return self._handle_function_inplace(other, operator.sub)

    def __mul__(self, other):
        return self._handle_left_operand_function(other, operator.mul)

    def __rmul__(self, other):
        return self._handle_right_operand_function(other, operator.mul)

    def __imul__(self, other):
        return self._handle_function_inplace(other, operator.mul)

    def __floordiv__(self, other):
        return self._handle_left_operand_function(other, operator.floordiv)

    def __rfloordiv__(self, other):
        return self._handle_right_operand_function(other, operator.floordiv)

    def __ifloordiv__(self, other):
        return self._handle_function_inplace(other, operator.floordiv)

    def __truediv__(self, other):
        return self._handle_left_operand_function(other, operator.truediv)

    def __rtruediv__(self, other):
        return self._handle_right_operand_function(other, operator.truediv)

    def __itruediv__(self, other):
        return self._handle_function_inplace(other, operator.floordiv)

    def __mod__(self, other):
        return self._handle_left_operand_function(other, operator.mod)

    def __rmod__(self, other):
        return self._handle_right_operand_function(other, operator.mod)

    def __pow__(self, other):
        return self._handle_left_operand_function(other, operator.pow)

    def __rpow__(self, other):
        return self._handle_right_operand_function(other, operator.pow)

    def __lshift__(self, other):
        return self._handle_left_operand_function(other, operator.lshift)

    def __rlshift__(self, other):
        return self._handle_right_operand_function(other, operator.lshift)

    def __rshift__(self, other):
        return self._handle_left_operand_function(other, operator.rshift)

    def __rrshift__(self, other):
        return self._handle_right_operand_function(other, operator.rshift)

    def __and__(self, other):
        return self._handle_left_operand_function(other, operator.and_)

    def __rand__(self, other):
        return self._handle_right_operand_function(other, operator.and_)

    def __or__(self, other):
        return self._handle_left_operand_function(other, operator.or_)

    def __ror__(self, other):
        return self._handle_right_operand_function(other, operator.or_)

    def __xor__(self, other):
        return self._handle_left_operand_function(other, operator.xor)

    def __rxor__(self, other):
        return self._handle_right_operand_function(other, operator.xor)

    def __neg__(self):
        return Vector2D(operator.neg(self.x), operator.neg(self.y))

    def __pos__(self):
        return Vector2D(operator.pos(self.x), operator.pos(self.y))

    def __abs__(self):
        return Vector2D(abs(self.x), abs(self.y))

    def __invert__(self):
        return Vector2D(-self.x, -self.y)

    def __round__(self, digits=0):
        return Vector2D(round(self.x, digits), round(self.y, digits))

    def get_angle_between(self, other):
        return math.degrees(math.atan2(self.cross(other), self.dot(other)))

    def normalize(self):
        length = self.length
        if length == 0:
            return Vector2D(self.x, self.y)
        return self / length

    def get_perpendicular(self):
        return Vector2D(-self.y, self.x)

    def dot(self, other):
        return self.x * other[0] + self.y * other[1]

    def get_squared_distance(self, other):
        return (self.x - other[0]) ** 2 + (self.y - other[1]) ** 2

    def get_distance(self, other):
        return math.sqrt(self.get_squared_distance(other))

    def project(self, other):
        other_squared_length = other[0] * other[0] + other[1] * other[1]
        projected_length = self.dot(other)
        return other * (projected_length / other_squared_length)

    def cross(self, other):
        return self.x * other[1] - self.y * other[0]

    def interpolate_to(self, other, interpolation_range):
        return Vector2D(self.x + (other[0] - self.x) * interpolation_range,
                        self.y + (other[1] - self.y) * interpolation_range)

    def convert_to_basis(self, x_vector, y_vector):
        """

        :type x_vector: Vector2D
        :type y_vector: Vector2D
        :rtype: Vector2D
        """
        return Vector2D(self.dot(x_vector) / x_vector.squared_length,
                        self.dot(y_vector) / y_vector.squared_length)

    def __getstate__(self):
        return self.x, self.y

    def __setstate__(self, coordinates):
        self.x, self.y = coordinates
