import math

from constants import BLACK
from tools.shape_tool import ShapeTool


class FilledCircle(ShapeTool):
    def draw_icon(self, drawer, x, y):
        center_x, center_y = x + 25, y + 25
        for dy in range(-14, 15):
            dx = int(math.sqrt(14 * 14 - dy * dy))
            drawer.fill_rect(center_x - dx, center_y + dy, center_x + dx + 1, center_y + dy + 1, BLACK)

    def draw_shape(self, drawer, state, center_x, center_y, x, y):
        radius = int(math.hypot(x - center_x, y - center_y))

        for dy in range(-radius, radius + 1):
            dx = int(math.sqrt(radius * radius - dy * dy))
            drawer.fill_canvas_rect(center_x - dx, center_y + dy, center_x + dx + 1, center_y + dy + 1, state.color)