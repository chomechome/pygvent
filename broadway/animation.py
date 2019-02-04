import collections
from typing import Sequence, Iterator

from broadway.picture import IPicture
from broadway.types import Seconds
from broadway.utils.slots import Slots


class Frame(collections.namedtuple('Frame', 'image duration')):
    __slots__ = ()

    def __new__(cls, image: IPicture, duration: Seconds):
        assert duration > 0

        return super().__new__(cls, image, duration)


class Animation(Slots):
    __slots__ = '_frames',

    def __init__(self, frames: Sequence[Frame]):
        assert frames

        self._frames = frames

    def __len__(self):
        return len(self._frames)

    def __iter__(self) -> Iterator[Frame]:
        return iter(self._frames)

    def __getitem__(self, item: int) -> Frame:
        return self._frames[item]

    @property
    def duration(self):
        return sum(frame.duration for frame in self._frames)
