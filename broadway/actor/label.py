from broadway.actor import Actor
from broadway.alignment import Alignment
from broadway.picture.text import Text


class Label(Actor):
    def __init__(self,
                 image: Text,
                 alignment: Alignment = Alignment.BOTTOMLEFT,
                 **kwargs
                 ):
        super().__init__(image=image, **kwargs)

        self.alignment = alignment

    def draw(self):
        width, height = self.image.resolution
        position = self.alignment.align(self.position, width, height)
        self.image.draw(position)
