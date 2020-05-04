from pygvent.actor import Actor
from pygvent.geometry import Vector


class Projectile(Actor):

    _DIRECTION = Vector(0, -10)

    def update(self, elapsed):
        self.transform.translate(self._DIRECTION)
