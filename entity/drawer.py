from constants import CANVAS_WIDTH, CANVAS_HEIGHT, TOOLBAR_WIDTH, WIDTH, HEIGHT


class Drawer:
    def __init__(self, pixels):
        self.pixels = pixels

    def put_pixel(self, x, y, color):
        height, width = HEIGHT, WIDTH

        if 0 <= x < width and 0 <= y < height:
            self.pixels[y, x] = color

    def get_pixel(self, x, y):
        height, width, _ = self.pixels.shape

        if 0 <= x < width and 0 <= y < height:
            return tuple(self.pixels[y, x].tolist())
        return None

    # FILL RECTANGLE
    def fill_rect(self, x1, y1, x2, y2, color):
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.put_pixel(x, y, color)

    def fill_canvas_rect(self, x1, y1, x2, y2, color):
        x1 = max(x1, TOOLBAR_WIDTH)
        x2 = min(x2, WIDTH)
        y1 = max(y1, 0)
        y2 = min(y2, CANVAS_HEIGHT)

        if x1 >= x2 or y1 >= y2:
            return

        self.fill_rect(x1, y1, x2, y2, color)

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

    # LINE
    def bresenham_line(self, start_x, start_y, end_x, end_y, color, thickness=1):
        distance_x = abs(end_x - start_x)
        distance_y = abs(end_y - start_y)
        step_x = 1 if start_x < end_x else -1
        step_y = 1 if start_y < end_y else -1
        error = distance_x - distance_y

        x, y = start_x, start_y
        while True:
            self.thick_pixel(x, y, color, thickness)
            if x == end_x and y == end_y:
                break

            double_error = 2 * error
            if double_error > -distance_y:
                error -= distance_y
                x += step_x
            if double_error < distance_x:
                error += distance_x
                y += step_y

    # BUCKET
    def flood_fill(self, x, y, color):
        old_color = tuple(self.pixels[y, x])
        if old_color == color:
            return

        stack = [(x, y)]

        while stack:
            x, y = stack.pop()

            inside_canvas = TOOLBAR_WIDTH <= x < TOOLBAR_WIDTH + CANVAS_WIDTH and 0 <= y < CANVAS_HEIGHT
            if not inside_canvas:
                continue

            if tuple(self.pixels[y, x]) != old_color:
                continue

            self.pixels[y, x] = color

            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))