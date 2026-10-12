from constants import BLACK, PINK, BACKGROUND_COLOR
from tools.tool import Tool


class Eraser(Tool):
    def __init__(self):
        self.last = None

    def draw_icon(self, drawer, x, y):
        drawer.fill_rect(x + 10, y + 20, x + 40, y + 38, BLACK)
        drawer.fill_rect(x + 12, y + 22, x + 38, y + 36, PINK)

    def press(self, drawer, state, x, y):
        drawer.thick_pixel(x, y, BACKGROUND_COLOR, state.thickness)
        self.last = (x, y)

    def drag(self, drawer, state, x, y):
        last_x, last_y = self.last
        drawer.bresenham_line(last_x, last_y, x, y, BACKGROUND_COLOR, state.thickness)
        self.last = (x, y)
