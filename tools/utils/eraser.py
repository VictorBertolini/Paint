from constants import BLACK, PINK, BACKGROUND_COLOR
from tools.tool import Tool


class Eraser(Tool):
    def __init__(self):
        self.last = None

    def draw_icon(self, drawer, x, y):
        # parte traseira
        drawer.fill_rect(x + 12, y + 28, x + 22, y + 40, BLACK)
        drawer.fill_rect(x + 14, y + 30, x + 22, y + 38, PINK)

        # parte central
        drawer.fill_rect(x + 22, y + 24, x + 32, y + 36, BLACK)
        drawer.fill_rect(x + 22, y + 26, x + 30, y + 34, PINK)

        # ponta da borracha
        drawer.fill_rect(x + 32, y + 20, x + 40, y + 32, BLACK)
        drawer.fill_rect(x + 32, y + 22, x + 38, y + 30, BLACK)

        # detalhe inferior
        drawer.fill_rect(x + 18, y + 38, x + 34, y + 40, BLACK)

    def press(self, drawer, state, x, y):
        drawer.thick_pixel(x, y, BACKGROUND_COLOR, state.thickness)
        self.last = (x, y)

    def drag(self, drawer, state, x, y):
        last_x, last_y = self.last
        drawer.bresenham_line(last_x, last_y, x, y, BACKGROUND_COLOR, state.thickness)
        self.last = (x, y)
