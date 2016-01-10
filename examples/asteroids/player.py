# coding=utf-8
from collections import namedtuple

from examples.asteroids.projectile import Projectile
from pygvent.objects import VisibleGameObject
from pygvent.utils.image import convert_to_mask
from pygvent.vector2d import Vector2D


class Player(VisibleGameObject):
    class State(object):
        NORMAL = 'normal'
        DESTROYED = 'destroyed'

    Images = namedtuple('PlayerImages', [State.NORMAL, State.DESTROYED])

    def __init__(self, position, images, **kwargs):
        super(Player, self).__init__(position, **kwargs)
        self.speed = 7
        self.state = Player.State.NORMAL
        self.images = images
        self.image = getattr(self.images, self.state)
        self.mask = convert_to_mask(self.image)

        self._left_move = (-self.speed, 0)
        self._right_move = (self.speed, 0)
        self._direction = Vector2D.zeros()
        self._destroyed_animation_frames = 10
        self._is_destroyed = False

    def update(self):
        if self._is_destroyed:
            if self._destroyed_animation_frames == 0:
                self.kill()
            else:
                self._destroyed_animation_frames -= 1
        elif self._is_enabled:
            if self.state is Player.State.DESTROYED:
                self.image = getattr(self.images, self.state)
                self._is_destroyed = True

    def draw(self, screen):
        if self.can_move(screen):
            self.move(self._direction)
        self._direction = Vector2D.zeros()

        super(Player, self).draw(screen)

    def can_move(self, screen):
        width, _ = screen.get_size()
        return (0 <= (self._position + self._direction).x <=
                width - self.rect.width
                and not self._is_destroyed)

    def move_left(self):
        self._direction += self._left_move

    def move_right(self):
        self._direction += self._right_move

    def shoot(self, projectiles, image):
        offset = (self.rect.width // 2 - 4, -6)
        projectile = Projectile(self.position + offset, image)
        projectiles.add(projectile)
