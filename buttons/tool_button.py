from buttons.button import Button


class ToolButton(Button):
    def __init__(self, x, y, width, height, tool):
        super().__init__(x, y, width, height)
        self.tool = tool

    def is_selected(self, state):
        return state.tool is self.tool

    def draw(self, drawer, state):
        super().draw(drawer, state)

    def draw_icon(self, drawer):
        self.tool.draw_icon(drawer, self.x, self.y)

    def click(self, state):
        state.tool = self.tool