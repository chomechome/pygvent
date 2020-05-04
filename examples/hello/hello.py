from pygvent.actor import Label
from pygvent.alignment import Alignment
from pygvent.color import Color
from pygvent.game import Game
from pygvent.geometry import Point
from pygvent.picture import Text
from pygvent.structure import Scene


class HelloWorld(Game):
    def load(self):
        font = self.engine.get_font('resource/arial.ttf')
        resolution = self.display.get_resolution()

        text = Text(
            font=font,
            text='Hello, world!',
            size=24,
            color=Color.WHITE,
        )
        label = Label(
            text,
            position=Point(resolution.width / 2, resolution.height / 2),
            alignment=Alignment.CENTER,
        )
        return Scene(nodes=[label])


if __name__ == "__main__":
    HelloWorld(caption='Hello, world!').run()
