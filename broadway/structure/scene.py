from typing import Iterable

from broadway.structure.node import Node
from broadway.types import Seconds


class Scene:
    def __init__(self, nodes: Iterable[Node] = ()):
        self.root = Node()

        for node in nodes:
            self.root.attach(node)

    def update(self, elapsed: Seconds):
        for node in self.root.walk():
            node.update(elapsed)

        self.transform()

    def draw(self):
        for node in self.root.walk():
            node.draw()

    def transform(self):
        root = self.root
        root_transform = root.transform

        if root_transform.is_outdated:
            root_transform.world = root_transform.local.copy()

        for child in root.children:
            self._transform(root, child)

        root_transform.is_outdated = False

    def _transform(self, parent: Node, node: Node):
        node_transform = node.transform
        parent_transform = parent.transform

        if parent_transform.is_outdated or node_transform.is_outdated:
            node_transform.combine(parent_transform)

        for child in node.children:
            self._transform(node, child)

        node_transform.is_outdated = False
