import numpy as np

from constants import BLACK, CANVAS_HEIGHT, CANVAS_WIDTH, GRAY, TOOLBAR_WIDTH
from tools.tool import Tool


class Bucket(Tool):
    def draw_icon(self, drawer, x, y):
        # Alça do balde
        drawer.fill_rect(x + 18, y + 12, x + 20, y + 19, BLACK)
        drawer.fill_rect(x + 20, y + 9, x + 30, y + 12, BLACK)
        drawer.fill_rect(x + 30, y + 12, x + 32, y + 19, BLACK)

        # Corpo do balde, afunilando na base
        for row in range(21, 40):
            inset = (row - 21) // 6
            left = x + 12 + inset
            right = x + 38 - inset

            drawer.fill_rect(left, y + row, right, y + row + 1, BLACK)
            drawer.fill_rect(
                left + 3, y + row,
                right - 3, y + row + 1, GRAY
            )

        # Borda superior
        drawer.fill_rect(x + 10, y + 19, x + 40, y + 23, BLACK)
        drawer.fill_rect(x + 13, y + 20, x + 37, y + 21, GRAY)

        # Brilho na lateral
        drawer.fill_rect(x + 19, y + 26, x + 21, y + 34, BLACK)

        # Base
        drawer.fill_rect(x + 15, y + 39, x + 35, y + 41, BLACK)

    def press(self, drawer, state, x, y):
        drawer.flood_fill(x, y, state.color)