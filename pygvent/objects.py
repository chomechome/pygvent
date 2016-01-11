from abc import ABCMeta, abstractmethod
from pygvent.events import Event
from pygvent.vector2d import Vector2D


# TODO: add frame to scene and objects for time control?
class GameObject(object):
    __metaclass__ = ABCMeta

    def __init__(self, layers=None, is_enabled=True):
        """

        :type layers: list[pygvent.structures.Layer]
        :type is_enabled: bool
        """
        self.on_kill = Event()

        self._layers = set()
        self._is_enabled = is_enabled

        for layer in layers or []:
            self.add_to_layer(layer)

    @property
    def layers(self):
        return self._layers

    def add_to_layer(self, layer):
        layer.add(self)
        self._layers.add(layer)

    def remove_from_layer(self, layer):
        if self in layer:
            layer.remove(self)
        if layer in self._layers:
            self._layers.remove(layer)

    def clear_layers(self):
        while self._layers:
            self._layers.pop().remove(self)

    def kill(self):
        self.clear_layers()
        self.on_kill()

    def disable(self):
        self._is_enabled = False

    def enable(self):
        self._is_enabled = True

    @abstractmethod
    def update(self):
        pass


class VisibleGameObject(GameObject):
    __metaclass__ = ABCMeta

    def __init__(self, position, image=None, image_mask=None, layers=None,
                 is_enabled=True, is_visible=True, is_static=False):
        """

        :param image: An image to use as object visualization
        :param image_mask: Defines which pixels of image to use when object
        is checked for intersection
        :type position: pygvent.vector2d.Vector2D|list|tuple
        :type is_visible: bool
        :type is_static: bool
        """
        super(VisibleGameObject, self).__init__(layers, is_enabled)
        self.image = image
        self.mask = image_mask

        self._is_visible = is_visible
        self._is_static = is_static
        self._position = Vector2D.convert(position)

    @property
    def position(self):
        return self._position

    @property
    def rect(self):
        bounding_box = self.image.get_rect()
        bounding_box.x = self._position.x
        bounding_box.y = self._position.y
        return bounding_box

    def hide(self):
        self._is_visible = False

    def show(self):
        self._is_visible = True

    def move(self, offset):
        if not self._is_static:
            self._position += offset

    def draw(self, screen):
        if self._is_visible and self.image is not None:
            screen.blit(self.image, self.position)

    @abstractmethod
    def update(self):
        pass
