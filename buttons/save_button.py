from buttons.action_button import ActionButton
from constants import BLACK, GRAY, WHITE, DARK_GRAY


class SaveButton(ActionButton):
    def draw_icon(self, drawer):
        x = self.x
        y = self.y

        # corpo externo
        drawer.fill_rect(x + 12, y + 10, x + 38, y + 40, BLACK)

        # área interna
        drawer.fill_rect(x + 14, y + 12, x + 36, y + 38, GRAY)

        # etiqueta superior
        drawer.fill_rect(x + 17, y + 15, x + 29, y + 22, WHITE)

        # trava / detalhe no topo direito
        drawer.fill_rect(x + 30, y + 14, x + 34, y + 23, DARK_GRAY)

        # abertura inferior
        drawer.fill_rect(x + 19, y + 27, x + 31, y + 36, BLACK)
        drawer.fill_rect(x + 21, y + 29, x + 29, y + 34, WHITE)