import abc

from broadway.structure import Scene


class IGameLoop(metaclass=abc.ABCMeta):
    __slots__ = ()

    @abc.abstractmethod
    def run(self, scene: Scene):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
