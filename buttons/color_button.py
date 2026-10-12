from buttons.button import Button


class ColorButton(Button):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color

    def is_selected(self, state):
        return state.color == self.color

    def inner_color(self):
        return self.color

    def click(self, state):
        state.color = self.color