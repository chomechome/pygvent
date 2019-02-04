from typing import List

from broadway.action import IAction
from broadway.geometry import Point
from broadway.picture import IPicture
from broadway.structure import Node
from broadway.types import Seconds


class Actor(Node):
    def __init__(self,
                 image: IPicture,
                 position: Point,
                 is_enabled: bool = True,
                 is_visible: bool = True,
                 ):
        super().__init__()

        self.image = image
        self.position = position
        self.is_enabled = is_enabled
        self.is_visible = is_visible

        self._anchor = position.copy()
        self._actions: List[IAction] = []

    def do(self, action: IAction):
        self._actions.append(action)

    def stop(self, action: IAction):
        self._actions.remove(action)

    def update(self, elapsed: Seconds):
        for action in self._actions:
            action.update(self, elapsed)

        self._actions = [action for action in self._actions
                         if not action.is_done]

    def draw(self):
        self.position = self.transform.apply(self._anchor)
        self.image.draw(self.position)
