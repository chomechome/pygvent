# coding=utf-8
from collections import OrderedDict


class Layer(object):
    def __init__(self, name, objects=None):
        """

        :type name: str
        :type objects: collections.Iterable[pygvent.objects.GameObject]
        """
        self.name = name

        self._objects = set()

        self.extend(objects or [])

    def __iter__(self):
        return iter(self._objects.copy())

    def __contains__(self, item):
        return item in self._objects

    def __len__(self):
        return len(self._objects)

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        """

        :type other: Layer
        :rtype: bool
        """
        if type(self) is type(other):
            return self.name == other.name and self._objects == other._objects
        return False

    @property
    def objects(self):
        return self._objects

    def add(self, obj):
        obj.layers.add(self)
        self._objects.add(obj)

    def remove(self, obj):
        if self in obj.layers:
            obj.layers.remove(self)
        if obj in self:
            self._objects.remove(obj)

    def extend(self, iterable):
        for obj in iterable:
            self.add(obj)

    def clear(self):
        for obj in self:
            self.remove(obj)

    def copy(self):
        return Layer(self.name, self._objects)

    def update(self):
        for obj in self:
            obj.update()

    def draw(self, screen):
        for obj in self:
            obj.draw(screen)


class Scene(object):
    def __init__(self, layers=None):
        """

        :type layers: collections.Iterable[Layer]
        """
        self._layers_dictionary = OrderedDict()

        self.extend(layers or [])

    def __len__(self):
        return len(self._layers_dictionary)

    def __contains__(self, item):
        return item in self.layers

    def __iter__(self):
        """

        :rtype: collections.Iterable[Layer]
        """
        return iter(self.layers)

    # TODO: this is a hack for already deleted layers, might not be good
    def __getitem__(self, item):
        """

        :type item: str
        :rtype: collections.Iterable[pygvent.objects.GameObject]
        """
        return self._layers_dictionary.get(item, [])

    def __getattr__(self, item):
        if item in self._layers_dictionary:
            return self[item]
        message = "'{}' object has no attribute '{}'".format(type(self), item)
        raise AttributeError(message)

    @property
    def layers(self):
        return list(self._layers_dictionary.values())

    @property
    def layer_names(self):
        return list(self._layers_dictionary.keys())

    @property
    def object_count(self):
        return sum(map(len, self))

    def add(self, layer):
        self._layers_dictionary[layer.name] = layer

    def remove(self, layer):
        """

        :type layer: str|Layer
        """
        if isinstance(layer, str):
            self._layers_dictionary.pop(layer)
        else:
            self._layers_dictionary.pop(layer.name)

    def extend(self, layers):
        for layer in layers:
            self.add(layer)

    def clear(self):
        for layer in self:
            layer.clear()
        self._layers_dictionary.clear()

    def update(self):
        for layer in self:
            layer.update()

    def draw(self, screen):
        for layer in self:
            layer.draw(screen)
