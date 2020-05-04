from typing import Optional

from pygvent.geometry.point import Point
from pygvent.types import Area, Coordinate
from pygvent.utils.slots import Slots


class Rectangle(Slots):
    __slots__ = 'left', 'bottom', 'width', 'height'

    def __init__(self,
                 left: Coordinate,
                 bottom: Coordinate,
                 width: float,
                 height: float,
                 ):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height

    @classmethod
    def from_coordinates(cls,
                         left: Coordinate,
                         bottom: Coordinate,
                         right: Coordinate,
                         top: Coordinate,
                         ):
        return cls(left, bottom, width=right - left, height=top - bottom)

    @classmethod
    def from_points(cls, bottomleft: Point, topright: Point):
        return cls(
            left=bottomleft.x,
            bottom=bottomleft.y,
            width=topright.x - bottomleft.x,
            height=topright.y - bottomleft.y,
        )

    @property
    def top(self) -> Coordinate:
        return self.bottom + self.height

    @property
    def right(self) -> Coordinate:
        return self.left + self.width

    @property
    def area(self) -> Area:
        return self.width * self.height

    @property
    def center(self) -> Point:
        return Point(self.left + self.width / 2, self.bottom + self.height / 2)

    @property
    def topleft(self) -> Point:
        return Point(self.left, self.top)

    @property
    def topright(self) -> Point:
        return Point(self.right, self.top)

    @property
    def bottomleft(self) -> Point:
        return Point(self.left, self.bottom)

    @property
    def bottomright(self) -> Point:
        return Point(self.right, self.bottom)

    @property
    def midtop(self) -> Point:
        return Point(self.left + self.width / 2, self.top)

    @property
    def midbottom(self) -> Point:
        return Point(self.left + self.width / 2, self.bottom)

    @property
    def midleft(self) -> Point:
        return Point(self.left, self.bottom + self.height / 2)

    @property
    def midright(self) -> Point:
        return Point(self.right, self.bottom + self.height / 2)

    def __repr__(self):
        return '{}(left={}, bottom={}, width={}, height={})'.format(
            type(self).__name__,
            self.left,
            self.bottom,
            self.width,
            self.height,
        )

    def __eq__(self, other):
        return (
            isinstance(other, Rectangle) and
            self.left == other.left and
            self.bottom == other.bottom and
            self.width == other.width and
            self.height == other.height
        )

    def __bool__(self):
        return self.width != 0 and self.height != 0

    def __contains__(self, item):
        if isinstance(item, Point):
            return (self.left <= item.x <= self.right and
                    self.bottom <= item.y <= self.top)
        if isinstance(item, Rectangle):
            return self.intersect(item) == item
        return False

    def __copy__(self):
        return type(self)(self.left, self.bottom, self.width, self.height)

    copy = __copy__

    def intersects(self, rectangle: 'Rectangle') -> bool:
        return (
            self.left < rectangle.right and
            self.right > rectangle.left and
            self.bottom < rectangle.top and
            self.top > rectangle.bottom
        )

    def intersect(self, rectangle: 'Rectangle') -> Optional['Rectangle']:
        if not self.intersects(rectangle):
            return None
        return self.from_coordinates(
            left=max(self.left, rectangle.left),
            bottom=max(self.bottom, rectangle.bottom),
            right=min(self.right, rectangle.right),
            top=min(self.top, rectangle.top),
        )
