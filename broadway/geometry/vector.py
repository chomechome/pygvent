import math

from broadway.types import Degrees, Coordinate
from broadway.utils.slots import Slots


class Vector(Slots):
    __slots__ = 'x', 'y'

    def __init__(self, x: Coordinate, y: Coordinate):
        self.x = x
        self.y = y

    @classmethod
    def zeros(cls):
        return cls(0, 0)

    @classmethod
    def ones(cls):
        return cls(1, 1)

    @property
    def squared_length(self) -> float:
        return self.x * self.x + self.y * self.y

    @property
    def length(self) -> float:
        return math.sqrt(self.squared_length)

    @length.setter
    def length(self, value: float):
        length = self.length
        if length == 0:
            self.x = value
        else:
            self.x *= value / length
            self.y *= value / length

    @property
    def angle(self) -> Degrees:
        if self.squared_length == 0:
            return 0
        return math.degrees(math.atan2(self.y, self.x))

    @angle.setter
    def angle(self, angle: Degrees):
        self.x = self.length
        self.y = 0
        self.rotate(angle, inplace=True)

    @property
    def normalized(self) -> 'Vector':
        length = self.length
        if length:
            return self / length
        return self.copy()

    @property
    def perpendicular(self) -> 'Vector':
        return Vector(-self.y, self.x)

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __eq__(self, other) -> bool:
        return (isinstance(other, Vector) and
                self.x == other.x and
                self.y == other.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __iter__(self):
        yield self.x
        yield self.y

    def __copy__(self):
        return Vector(self.x, self.y)

    copy = __copy__

    def __add__(self, vector: 'Vector') -> 'Vector':
        return Vector(self.x + vector.x, self.y + vector.y)

    def __iadd__(self, other: 'Vector') -> 'Vector':
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, vector: 'Vector') -> 'Vector':
        return Vector(self.x - vector.x, self.y - vector.y)

    def __isub__(self, vector: 'Vector') -> 'Vector':
        self.x -= vector.x
        self.y -= vector.y
        return self

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __imul__(self, scalar: float) -> 'Vector':
        self.x *= scalar
        self.y *= scalar
        return self

    def __truediv__(self, scalar: float) -> 'Vector':
        return Vector(self.x / scalar, self.y / scalar)

    def __itruediv__(self, scalar: float) -> 'Vector':
        self.x /= scalar
        self.y /= scalar
        return self

    def __neg__(self):
        return type(self)(-self.x, -self.y)

    def __abs__(self):
        return type(self)(abs(self.x), abs(self.y))

    def get_angle(self, vector: 'Vector') -> Degrees:
        return math.degrees(math.atan2(self.cross(vector), self.dot(vector)))

    def rotate(self, angle: Degrees, inplace: bool = False) -> 'Vector':
        """
        :param inplace: If True, method changes current instance
        """
        radians = math.radians(angle)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos

        if not inplace:
            return Vector(x, y)

        self.x = x
        self.y = y
        return self

    def dot(self, vector: 'Vector') -> float:
        return self.x * vector.x + self.y * vector.y

    def cross(self, vector: 'Vector') -> float:
        return self.x * vector.y - self.y * vector.x
