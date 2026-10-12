from constants import CANVAS_WIDTH, CANVAS_HEIGHT, TOOLBAR_WIDTH


class Drawer:
    def __init__(self, pixels):
        self.pixels = pixels

    # FILL RECTANGLE
    def fill_rect(self, x1, y1, x2, y2, color):
        self.pixels[y1:y2, x1:x2] = color

    def fill_canvas_rect(self, x1, y1, x2, y2, color):
        x1 = max(x1, TOOLBAR_WIDTH)
        x2 = min(x2, TOOLBAR_WIDTH + CANVAS_WIDTH)
        y1 = max(y1, 0)
        y2 = min(y2, CANVAS_HEIGHT)

        if x1 >= x2 or y1 >= y2:
            return

        self.pixels[y1:y2, x1:x2] = color

    # RECTANGLE
    def canvas_rect(self, start_x, start_y, end_x, end_y, color, thickness=1):
        for i in range(end_x - start_x):
            self.thick_pixel(start_x + i, start_y, color, thickness)
            self.thick_pixel(start_x + i, end_y, color, thickness)

        for i in range(end_y - start_y):
            self.thick_pixel(start_x, start_y + i, color, thickness)
            self.thick_pixel(end_x, start_y + i, color, thickness)

    # THICK PIXEL
    def thick_pixel(self, x, y, color, thickness):
        half = thickness // 2
        self.fill_canvas_rect(x - half, y - half, x + half + 1, y + half + 1, color)


    def bresenham_line(self, x1, y1, x2, y2, color, thickness=1):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        x, y = x1, y1
        while True:
            self.thick_pixel(x, y, color, thickness)
            if x == x2 and y == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy