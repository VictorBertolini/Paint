from constants import BLACK
from tools.shape_tool import ShapeTool


class FilledRectangle(ShapeTool):
    def draw_icon(self, drawer, x, y):
        drawer.fill_rect(x + 10, y + 15, x + 40, y + 35, BLACK)

    def draw_shape(self, drawer, state, x1, y1, x2, y2):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        drawer.fill_canvas_rect(x1, y1, x2, y2, state.color)
