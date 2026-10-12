import glfw


class Mouse:
    def __init__(self, window):
        self.window = window
        self.was_pressed = False
        self.is_pressed = False

    def update(self):
        self.was_pressed = self.is_pressed
        self.is_pressed = glfw.get_mouse_button(self.window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS

    def pressed(self):
        return self.is_pressed

    def just_pressed(self):
        return self.is_pressed and not self.was_pressed

    def just_released(self):
        return self.was_pressed and not self.is_pressed

    def position(self):
        x, y = glfw.get_cursor_pos(self.window)
        return int(x), int(y)