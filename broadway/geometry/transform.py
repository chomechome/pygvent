import math

from broadway.geometry import Point, Vector, Matrix
from broadway.types import Degrees
from broadway.utils.slots import Slots


class Transform(Slots):
    __slots__ = 'local', 'world', 'is_outdated'

    def __init__(self):
        self.local = Matrix()
        self.world = Matrix()

        self.is_outdated = False

    def apply(self, position: Point) -> Point:
        matrix = self.world
        x = matrix.m11 * position.x + matrix.m12 * position.y + matrix.m13
        y = matrix.m21 * position.x + matrix.m22 * position.y + matrix.m23
        return Point(x, y)

    def translate(self, direction: Vector):
        self.local *= Matrix(m13=direction.x, m23=direction.y)

        self.is_outdated = True

    def scale(self, width: float, height: float):
        self.local *= Matrix(m11=width, m22=height)

        self.is_outdated = True

    def rotate(self, angle: Degrees):
        radians = math.radians(angle)
        cos = math.cos(radians)
        sin = math.sin(radians)
        self.local *= Matrix(m11=cos, m12=sin, m21=-sin, m22=cos)

        self.is_outdated = True

    def combine(self, parent: 'Transform'):
        self.world: Matrix = parent.world * self.local

        self.is_outdated = True
