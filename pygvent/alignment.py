import enum

from pygvent.geometry import Point


class Horizontal(enum.IntEnum):
    RIGHT = 1
    MIDDLE = 0
    LEFT = -1


class Vertical(enum.IntEnum):
    TOP = 1
    MIDDLE = 0
    BOTTOM = -1


class Alignment(enum.Enum):
    BOTTOMLEFT = Horizontal.LEFT, Vertical.BOTTOM
    BOTTOMRIGHT = Horizontal.RIGHT, Vertical.BOTTOM
    TOPLEFT = Horizontal.LEFT, Vertical.TOP
    TOPRIGHT = Horizontal.RIGHT, Vertical.TOP
    CENTER = Horizontal.MIDDLE, Vertical.MIDDLE
    MIDLEFT = Horizontal.LEFT, Vertical.MIDDLE
    MIDRIGHT = Horizontal.RIGHT, Vertical.MIDDLE
    MIDBOTTOM = Horizontal.MIDDLE, Vertical.BOTTOM
    MIDTOP = Horizontal.MIDDLE, Vertical.TOP

    @property
    def horizontal(self) -> Horizontal:
        return self.value[0]

    @property
    def vertical(self) -> Vertical:
        return self.value[1]

    def align(self, position: Point, width: int, height: int) -> Point:
        position = position.copy()

        horizontal = self.horizontal
        if horizontal is Horizontal.MIDDLE:
            position.x -= width / 2
        elif horizontal is Horizontal.RIGHT:
            position.x -= width

        vertical = self.vertical
        if vertical is Vertical.MIDDLE:
            position.y -= height / 2
        elif vertical is Vertical.TOP:
            position.y -= height

        return position
