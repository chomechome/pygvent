from broadway.geometry import Point
from broadway.structure import Node
from broadway.picture import IPicture


class Background(Node):
    def __init__(self, image: IPicture):
        super().__init__()

        self._image = image
        self._position = Point.zeros()

    def draw(self):
        self._image.draw(self._position)
