from constants import BLACK
from tools.tool import Tool


class Pencil(Tool):
    def __init__(self):
        self.last = None

    def draw_icon(self, drawer, x, y):
        for i in range(30):
            drawer.fill_rect(x + 10 + i, y + 40 - i, x + 13 + i, y + 43 - i, BLACK)

    def press(self, drawer, state, x, y):
        drawer.thick_pixel(x, y, state.color, state.thickness)
        self.last = (x, y)

    def drag(self, drawer, state, x, y):
        last_x, last_y = self.last
        drawer.bresenham_line(last_x, last_y, x, y, state.color, state.thickness)
        self.last = (x, y)