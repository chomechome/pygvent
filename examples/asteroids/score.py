from broadway.actor import Label
from broadway.alignment import Alignment
from broadway.color import Color
from broadway.font import IFont
from broadway.geometry import Point
from broadway.picture.text import Text


class AsteroidScore(Label):
    def __init__(self,
                 font: IFont,
                 position: Point,
                 alignment: Alignment = Alignment.TOPLEFT,
                 ):
        self._score = 0

        super().__init__(
            image=Text(
                font,
                text=self._get_text(),
                size=20,
                color=Color.WHITE,
            ),
            position=position,
            alignment=alignment,
        )

    def increase(self, value: int):
        self._score += value
        self.image.text = self._get_text()

    def _get_text(self) -> str:
        return 'Score: {}'.format(self._score)
