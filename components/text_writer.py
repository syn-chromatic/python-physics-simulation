from components.graphics import Graphics
from components.color import RGBA

from dataclasses import dataclass


@dataclass
class FontConfiguration:
    font_type: str
    font_size: int
    font_style: str
    font_color: RGBA
    line_height: float
    padding_percent: int

    @property
    def font_tuple(self) -> tuple[str, int, str]:
        return (self.font_type, self.font_size, self.font_style)


class TextWriter:
    def __init__(self, font: FontConfiguration):
        self.font = font
        self.tl_column = []

    def add_text_top_left(self, text: str):
        self.tl_column.append(text)

    @staticmethod
    def get_padded_top_left_corner(
        width: int, height: int, padding_x: float, padding_y: float
    ) -> tuple[float, float]:
        top_left_x = (-width / 2.0) + padding_x
        top_left_y = (height / 2.0) - padding_y
        return top_left_x, top_left_y

    def get_text_xy(self, width: int, height: int, idx: int) -> tuple[float, float]:
        font_size = self.font.font_size
        line_height = self.font.line_height
        padding_percent = self.font.padding_percent
        padding_x = width * (padding_percent / 100)
        padding_y = height * (padding_percent / 100)

        text_x = padding_x
        text_y = (font_size * line_height * idx) + (padding_y / line_height)

        text_xy = self.get_padded_top_left_corner(width, height, text_x, text_y)
        return text_xy

    def draw(self, graphics: Graphics):
        width = graphics.get_width()
        height = graphics.get_height()

        for idx, text in enumerate(self.tl_column, 1):
            text_xy = self.get_text_xy(width, height, idx)
            font_tuple = self.font.font_tuple
            font_color = self.font.font_color
            graphics.draw_text(text_xy, font_color, text, font_tuple)

        self.tl_column = []
