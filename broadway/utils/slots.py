from typing import Dict


class Slots:
    """
    Base class for hierarchies with slots
    """
    __slots__ = ()

    def __getstate__(self) -> Dict:
        return {slot: getattr(self, slot) for slot in self.__slots__}

    def __setstate__(self, state: Dict):
        for name, value in state.items():
            setattr(self, name, value)
