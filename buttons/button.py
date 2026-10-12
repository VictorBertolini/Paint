from constants import BLACK, DARK_GRAY, GRAY


class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, px, py):
        return self.x <= px < self.x + self.width and self.y <= py < self.y + self.height

    def is_selected(self, state):
        return False

    def draw(self, drawer, state):
        x2 = self.x + self.width
        y2 = self.y + self.height
        border = BLACK if self.is_selected(state) else DARK_GRAY
        drawer.fill_rect(self.x, self.y, x2, y2, border)
        drawer.fill_rect(self.x + 2, self.y + 2, x2 - 2, y2 - 2, self.inner_color())
        self.draw_icon(drawer)

    def draw_icon(self, drawer):
        pass

    def inner_color(self):
        return GRAY

    def click(self, state):
        pass