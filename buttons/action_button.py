from buttons.button import Button


class ActionButton(Button):
    def __init__(self, x, y, width, height, action):
        super().__init__(x, y, width, height)
        self.action = action

    def click(self, state):
        self.action()