from broadway.color import Color
from broadway.font import IFont
from broadway.geometry import Point
from broadway.picture import IPicture
from broadway.resolution import Resolution
from broadway.types import Degrees


class Text(IPicture):
    def __init__(self,
                 font: IFont,
                 text: str,
                 size: int,
                 color: Color.RGBA,
                 ):
        self._font = font
        self._text = text
        self._size = size
        self._color = color

        self._is_outdated = False
        self._image: IPicture = None

    @property
    def resolution(self):
        self._render()
        return self._image.resolution

    @property
    def text(self):
        return self._text

    @property
    def size(self):
        return self._size

    @property
    def color(self):
        return self._color

    @text.setter
    def text(self, text: str):
        self._text = text
        self._is_outdated = True

    @size.setter
    def size(self, size: int):
        self._size = size
        self._is_outdated = True

    @color.setter
    def color(self, color: Color.RGBA):
        self._color = color
        self._is_outdated = True

    def draw(self, position: Point):
        self._render()
        self._image.draw(position)

    def scale(self, resolution: Resolution):
        self._render()
        self._image.scale(resolution)

    def rotate(self, angle: Degrees):
        self._render()
        self._image.rotate(angle)

    def copy(self):
        return Text(self._font, self._text, self._size, self._color)

    def _render(self):
        if self._is_outdated or self._image is None:
            self._image = self._font.render(
                self._text,
                self._size,
                self._color,
            )
            self._is_outdated = False
