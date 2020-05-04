import collections


class Resolution(collections.namedtuple('Resolution', 'width height')):
    __slots__ = ()

    def __new__(cls, width: int, height: int):
        assert width > 0
        assert height > 0

        return super().__new__(cls, width, height)


HD = Resolution(1366, 768)
HD_PLUS = Resolution(1600, 1200)
HD_FULL = Resolution(1920, 1080)
