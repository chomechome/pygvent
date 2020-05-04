import abc

from pygvent.types import Seconds


class IAction(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def is_done(self) -> bool:
        pass

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def update(self, elapsed: Seconds) -> Seconds:
        pass


class IReversible(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reversed(self) -> IAction:
        pass
