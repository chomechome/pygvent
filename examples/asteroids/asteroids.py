import random
from typing import List

from broadway.actor import Actor
from broadway.geometry import Point, Vector, Rectangle
from broadway.structure import Node
from broadway.picture import IPicture
from broadway.types import Seconds


class Asteroid(Actor):

    _DIRECTION = Vector(0, -5)

    def update(self, elapsed: Seconds):
        self._move()

        super().update(elapsed)

    def _move(self):
        self.transform.translate(self._DIRECTION)
        self.transform.rotate(.5)


class AsteroidField(Node):
    def __init__(self,
                 area: Rectangle,
                 image: IPicture,
                 max_asteroids: int = 5,
                 spawn_periodicity: Seconds = .5,
                 ):
        super().__init__()

        self._image = image
        self._area = area
        self._max_asteroids = max_asteroids
        self._spawn_periodicity = spawn_periodicity

        resolution = image.resolution
        self._upper_bound = area.top + resolution.height
        self._lower_bound = area.bottom - resolution.height
        self._last_spawn: Seconds = 0

    def update(self, elapsed: Seconds):
        asteroids = self._get_asteroids()
        for asteroid in asteroids:
            if asteroid.position.y <= self._lower_bound:
                asteroid.detach()

        self._last_spawn += elapsed

        if len(asteroids) < self._max_asteroids:
            self._spawn()

    def _get_asteroids(self) -> List[Asteroid]:
        return [node for node in self._children if isinstance(node, Asteroid)]

    def _spawn(self):
        if self._last_spawn < self._spawn_periodicity:
            return

        width, height = self._image.resolution
        position = Point(
            x=random.randint(0, self._area.width - width),
            y=self._area.height + height - 100,
        )
        asteroid = Asteroid(
            image=self._image,
            position=position,
        )
        self.attach(asteroid)

        self._last_spawn = 0
