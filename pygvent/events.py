# coding=utf-8
import functools


class Event(object):
    def __init__(self):
        self._handlers = []

    @property
    def handlers(self):
        return self._handlers

    def __iadd__(self, handler):
        return self.add(handler)

    def add(self, handler):
        """

        :type handler: collections.Callable
        :rtype: Event
        """
        self._handlers.append(handler)
        return self

    def extend(self, handlers):
        self._handlers.extend(handlers)

    def __isub__(self, handler):
        return self.remove(handler)

    def remove(self, handler):
        """

        :type handler: collections.Callable
        :rtype: Event
        """
        handler = Handler.convert(handler)
        self._handlers = [x for x in self._handlers if x != handler]
        return self

    def remove_many(self, handlers):
        for handler in handlers:
            self.remove(handler)

    def __call__(self, *args, **kwargs):
        for handler in self._handlers:
            handler(*args, **kwargs)

    def clear(self):
        self._handlers.clear()


class Handler(functools.partial):
    def __eq__(self, other):
        if isinstance(other, functools.partial):
            return self.func == other.func
        return self.func == other

    @classmethod
    def convert(cls, other):
        if isinstance(other, cls):
            return other
        if isinstance(other, functools.partial):
            args = other.args or []
            kwargs = other.keywords or {}
            return cls(other.func, *args, **kwargs)
        return cls(other)
