from pygvent.geometry import Vector
from pygvent.types import Coordinate, Distance
from pygvent.utils.slots import Slots


class Point(Slots):
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

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other) -> bool:
        return (isinstance(other, Point) and
                self.x == other.x and
                self.y == other.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __iter__(self):
        yield self.x
        yield self.y

    def __copy__(self):
        return Point(self.x, self.y)

    copy = __copy__

    def __add__(self, vector: 'Vector') -> 'Point':
        return Point(self.x + vector.x, self.y + vector.y)

    def __iadd__(self, vector: 'Vector') -> 'Point':
        self.x += vector.x
        self.y += vector.y
        return self

    def __sub__(self, point: 'Point') -> 'Vector':
        return Vector(self.x - point.x, self.y - point.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def get_distance(self, point: 'Point') -> Distance:
        return (point - self).length
