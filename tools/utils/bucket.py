import numpy as np

from constants import BLACK, CANVAS_HEIGHT, CANVAS_WIDTH, GRAY, TOOLBAR_WIDTH
from tools.tool import Tool


class Bucket(Tool):
    def draw_icon(self, drawer, x, y):
        drawer.fill_rect(x + 12, y + 18, x + 36, y + 40, BLACK)
        drawer.fill_rect(x + 15, y + 21, x + 33, y + 37, GRAY)
        drawer.fill_rect(x + 36, y + 24, x + 41, y + 28, BLACK)

    def press(self, drawer, state, x, y):
        drawer.flood_fill(x, y, state.color)