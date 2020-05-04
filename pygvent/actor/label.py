from pygvent.actor import Actor
from pygvent.alignment import Alignment
from pygvent.picture.text import Text


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
