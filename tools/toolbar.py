from constants import TOOLBAR_WIDTH, HEIGHT, DARK_GRAY


class Toolbar:
    def __init__(self, state):
        self.state = state
        self.buttons = []

    def add(self, button):
        self.buttons.append(button)

    def draw(self, drawer):
        drawer.fill_rect(0, 0, TOOLBAR_WIDTH, HEIGHT, DARK_GRAY)
        for button in self.buttons:
            button.draw(drawer, self.state)

    def click(self, x, y):
        for button in self.buttons:
            if button.contains(x, y):
                button.click(self.state)