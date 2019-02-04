import pygame

from broadway.geometry import Point
from broadway.picture import IPicture
from broadway.resolution import Resolution
from broadway.types import Degrees


class PygamePicture(IPicture):
    __slots__ = '_screen', '_image'

    def __init__(self, screen: pygame.Surface, image: pygame.Surface):
        self._screen = screen
        self._image = image

    @property
    def resolution(self):
        width, height = self._image.get_size()
        return Resolution(width, height)

    def draw(self, position: Point):
        _, screen_height = self._screen.get_size()
        _, image_height = self._image.get_size()
        position = position.x, screen_height - image_height - position.y
        self._screen.blit(self._image, position)

    def scale(self, resolution: Resolution):
        self._image = pygame.transform.scale(self._image, resolution)

    def rotate(self, angle: Degrees):
        self._image = pygame.transform.rotate(self._image, angle)

    def copy(self):
        return PygamePicture(self._screen, self._image.copy())
