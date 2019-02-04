from typing import Optional, Iterator, List

from broadway.geometry import Transform
from broadway.types import Seconds
from broadway.utils.reference import WeakReference


class Node:
    def __init__(self):
        self.transform = Transform()

        self._parent: WeakReference[Node] = None
        self._children: List[Node] = []

    @property
    def children(self) -> Iterator['Node']:
        return iter(self._children)

    def get_parent(self) -> Optional['Node']:
        if self._parent is not None:
            parent: Node = self._parent()
            return parent
        return None

    def walk(self) -> Iterator['Node']:
        for child in self._children:
            yield child
            yield from child.walk()

    def attach(self, child: 'Node', index: int = None):
        child.detach()

        if index is None:
            self._children.append(child)
        else:
            self._children.insert(index, child)

        child._parent = WeakReference(self)

    def detach(self):
        parent = self.get_parent()

        if parent is not None:
            parent._children.remove(self)
            self._parent = None

    def update(self, elapsed: Seconds):
        pass

    def draw(self):
        pass
