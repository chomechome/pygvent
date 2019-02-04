from broadway.actor import Label
from broadway.alignment import Alignment
from broadway.color import Color
from broadway.game import Game
from broadway.geometry import Point
from broadway.picture import Text
from broadway.structure import Scene


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
