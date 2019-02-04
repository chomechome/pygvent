import pygame

from broadway.color import Color
from broadway.engine.pygame.picture import PygamePicture
from broadway.font import IFont


class PygameFont(IFont):
    def __init__(self, screen: pygame.Surface, path: str):
        self._screen = screen
        self._path = path

        self._size: int = None
        self._font: pygame.font.Font = None

    def render(self, text: str, size: int, color: Color.RGBA):
        if self._font is None or self._size != size:
            self._font = pygame.font.Font(self._path, size)
            self._size = size

        image = self._font.render(text, 0, pygame.Color(*color))
        return PygamePicture(self._screen, image)
