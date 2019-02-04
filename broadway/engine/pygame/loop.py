from typing import Callable, List

import pygame

from broadway.loop import IGameLoop
from broadway.structure import Scene
from broadway.types import FrameRate


class PygameLoop(IGameLoop):
    def __init__(self, rate: FrameRate):
        self._rate = rate

        self._clock = pygame.time.Clock()

    def run(self, scene: Scene):
        rate = self._rate
        clock = self._clock

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            elapsed = clock.tick(rate) / 1000

            scene.update(elapsed)
            scene.draw()
            pygame.display.flip()

    def stop(self):
        event = pygame.event.Event(pygame.QUIT, {})
        pygame.event.post(event)
