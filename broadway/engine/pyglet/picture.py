import pyglet

from broadway.geometry import Point
from broadway.picture import IPicture
from broadway.resolution import Resolution


class PygletPicture(IPicture):
    def __init__(self, image: pyglet.image.AbstractImage):
        self._image = image

    @property
    def resolution(self):
        return Resolution(self._image.width, self._image.height)

    def draw(self, position: Point):
        self._image.blit(position.x, position.y)
