from buttons.button import Button
from constants import BLACK


class ThicknessButton(Button):
    def __init__(self, x, y, width, height, thickness):
        super().__init__(x, y, width, height)
        self.thickness = thickness

    def is_selected(self, state):
        return state.thickness == self.thickness

    def click(self, state):
        state.thickness = self.thickness

    def draw(self, drawer, state):
        super().draw(drawer, state)

    def draw_icon(self, drawer):
        size = self.thickness * 3 + 1
        left = self.x + (self.width - size) // 2
        top = self.y + (self.height - size) // 2
        drawer.fill_rect(left, top, left + size, top + size, BLACK)