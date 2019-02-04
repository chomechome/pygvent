import pygame

from broadway.color import Color
from broadway.display import IDisplay
from broadway.resolution import Resolution


class PygameDisplay(IDisplay):
    def __init__(self, screen: pygame.Surface):
        self._screen = screen

    def get_caption(self) -> str:
        return pygame.display.get_caption()

    def set_caption(self, name: str):
        pygame.display.set_caption(name)

    def get_resolution(self) -> Resolution:
        width, height = self._screen.get_size()
        return Resolution(width, height)

    def set_resolution(self, resolution: Resolution):
        pygame.display.set_mode(resolution)

    def clear(self):
        self._screen.fill(Color.BLACK)
