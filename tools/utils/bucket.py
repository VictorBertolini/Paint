import numpy as np

from constants import BLACK, CANVAS_HEIGHT, CANVAS_WIDTH, GRAY, TOOLBAR_WIDTH
from tools.tool import Tool


class Bucket(Tool):
    def draw_icon(self, drawer, x, y):
        drawer.fill_rect(x + 12, y + 18, x + 36, y + 40, BLACK)
        drawer.fill_rect(x + 15, y + 21, x + 33, y + 37, GRAY)
        drawer.fill_rect(x + 36, y + 24, x + 41, y + 28, BLACK)

    def press(self, drawer, state, x, y):
        canvas = drawer.pixels[0:CANVAS_HEIGHT, TOOLBAR_WIDTH:TOOLBAR_WIDTH + CANVAS_WIDTH]
        start_x = x - TOOLBAR_WIDTH
        start_y = y

        target = canvas[start_y, start_x].copy()
        if (target == state.color).all():
            return

        same_color = (canvas == target).all(axis=2)
        filled = np.zeros_like(same_color)
        stack = [(start_x, start_y)]

        while stack:
            px, py = stack.pop()

            if not (0 <= px < CANVAS_WIDTH and 0 <= py < CANVAS_HEIGHT):
                continue
            if not same_color[py, px] or filled[py, px]:
                continue

            filled[py, px] = True
            stack.append((px + 1, py))
            stack.append((px - 1, py))
            stack.append((px, py + 1))
            stack.append((px, py - 1))

        canvas[filled] = state.color