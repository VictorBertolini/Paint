from constants import BLACK
from tools.shape_tool import ShapeTool


class Line(ShapeTool):
    def draw_icon(self, drawer, x, y):
        for i in range(30):
            drawer.fill_rect(x + 10 + i, y + 40 - i, x + 13 + i, y + 43 - i, BLACK)

    def draw_shape(self, drawer, state, x1, y1, x2, y2):
        drawer.bresenham_line(x1, y1, x2, y2, state.color, state.thickness)
