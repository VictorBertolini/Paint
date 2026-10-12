from constants import BLACK, GRAY
from tools.shape_tool import ShapeTool


class Rectangle(ShapeTool):
    def draw_icon(self, drawer, x, y):
        drawer.fill_rect(x + 10, y + 15, x + 40, y + 35, BLACK)
        drawer.fill_rect(x + 13, y + 18, x + 37, y + 32, GRAY)

    def draw_shape(self, drawer, state, x1, y1, x2, y2):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        half = state.thickness // 2
        left, right = x1 - half, x2 + half + 1
        top, bottom = y1 - half, y2 + half + 1

        drawer.fill_canvas_rect(left, top, right, y1 + half + 1, state.color)
        drawer.fill_canvas_rect(left, y2 - half, right, bottom, state.color)
        drawer.fill_canvas_rect(left, top, x1 + half + 1, bottom, state.color)
        drawer.fill_canvas_rect(x2 - half, top, right, bottom, state.color)