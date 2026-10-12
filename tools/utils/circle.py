import math

from constants import BLACK, GRAY
from tools.shape_tool import ShapeTool


class Circle(ShapeTool):
    def draw_icon(self, drawer, x, y):
        center_x, center_y = x + 25, y + 25
        for dy in range(-14, 15):
            dx = int(math.sqrt(14 * 14 - dy * dy))
            drawer.fill_rect(center_x - dx, center_y + dy, center_x + dx + 1, center_y + dy + 1, BLACK)
        for dy in range(-11, 12):
            dx = int(math.sqrt(11 * 11 - dy * dy))
            drawer.fill_rect(center_x - dx, center_y + dy, center_x + dx + 1, center_y + dy + 1, GRAY)

    def draw_shape(self, drawer, state, center_x, center_y, x, y):
        radius = int(math.hypot(x - center_x, y - center_y))
        px = 0
        py = radius
        d = 1 - radius

        while px <= py:
            for dx, dy in [(px, py), (-px, py), (px, -py), (-px, -py),
                           (py, px), (-py, px), (py, -px), (-py, -px)]:
                drawer.thick_pixel(center_x + dx, center_y + dy, state.color, state.thickness)

            if d < 0:
                d += 2 * px + 3
            else:
                d += 2 * (px - py) + 5
                py -= 1
            px += 1