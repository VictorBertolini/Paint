from buttons.action_button import ActionButton
from constants import BLACK, GRAY, ORANGE, YELLOW

class ClearButton(ActionButton):
    def draw_icon(self, drawer):
        x = self.x
        y = self.y

        # cabo diagonal (de cima à direita para baixo à esquerda)
        drawer.fill_rect(x + 30, y + 10, x + 33, y + 16, BLACK)
        drawer.fill_rect(x + 29, y + 16, x + 32, y + 22, BLACK)
        drawer.fill_rect(x + 28, y + 22, x + 31, y + 28, BLACK)
        drawer.fill_rect(x + 27, y + 28, x + 30, y + 32, BLACK)

        drawer.fill_rect(x + 31, y + 11, x + 32, y + 15, ORANGE)
        drawer.fill_rect(x + 30, y + 17, x + 31, y + 21, ORANGE)
        drawer.fill_rect(x + 29, y + 23, x + 30, y + 27, ORANGE)
        drawer.fill_rect(x + 28, y + 29, x + 29, y + 31, ORANGE)

        # junção do cabo com a cabeça
        drawer.fill_rect(x + 22, y + 30, x + 29, y + 33, BLACK)
        drawer.fill_rect(x + 23, y + 31, x + 28, y + 32, ORANGE)

        # cabeça da vassoura
        drawer.fill_rect(x + 14, y + 32, x + 28, y + 37, BLACK)
        drawer.fill_rect(x + 16, y + 33, x + 26, y + 36, YELLOW)

        # cerdas
        drawer.fill_rect(x + 15, y + 37, x + 17, y + 41, BLACK)
        drawer.fill_rect(x + 18, y + 37, x + 20, y + 41, BLACK)
        drawer.fill_rect(x + 21, y + 37, x + 23, y + 41, BLACK)
        drawer.fill_rect(x + 24, y + 37, x + 26, y + 41, BLACK)

        # poeira
        drawer.fill_rect(x + 31, y + 35, x + 34, y + 37, GRAY)
        drawer.fill_rect(x + 34, y + 37, x + 36, y + 39, GRAY)
        drawer.fill_rect(x + 30, y + 39, x + 32, y + 41, GRAY)