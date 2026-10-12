from tools.tool import Tool


class ShapeTool(Tool):
    def __init__(self):
        self.start = None
        self.saved = None

    def press(self, drawer, state, x, y):
        self.start = (x, y)
        self.saved = drawer.pixels.copy()

    def drag(self, drawer, state, x, y):
        drawer.pixels[:] = self.saved
        start_x, start_y = self.start
        self.draw_shape(drawer, state, start_x, start_y, x, y)

    def release(self, drawer, state, x, y):
        self.drag(drawer, state, x, y)