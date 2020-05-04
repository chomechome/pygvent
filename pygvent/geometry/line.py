from typing import Union

from pygvent.geometry.point import Point
from pygvent.geometry.vector import Vector
from pygvent.utils.slots import Slots


class Line(Slots):
    __slots__ = 'position', '_direction'

    def __init__(self, position: Point, direction: Vector):
        assert direction, "Line direction initialized with zero length vector"

        self.position = position
        self._direction = direction

    @classmethod
    def from_points(cls, first: Point, second: Point):
        return cls(first, second - first)

    @property
    def direction(self) -> Vector:
        return self._direction

    @direction.setter
    def direction(self, direction: Vector):
        assert direction, "Line direction set to zero length vector"

        self._direction = direction

    def __repr__(self):
        return '{}({} + u * {})'.format(
            type(self).__name__, self.position, self._direction,
        )

    def __contains__(self, item: Union[Point, Vector]) -> bool:
        if isinstance(item, Point):
            return ((item.x - self.position.x) * self._direction.y ==
                    (item.y - self.position.y) * self._direction.x)
        if isinstance(item, Vector):
            return abs(self._direction.normalized) == abs(item.normalized)
        return False

    def __eq__(self, other):
        return (isinstance(other, Line) and
                self.position in other and
                self._direction in other)
