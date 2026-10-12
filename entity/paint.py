import glfw
from OpenGL.GL import *
import numpy as np

from constants import CANVAS_HEIGHT, TOOLBAR_WIDTH, CANVAS_WIDTH, WHITE
from entity.drawer import Drawer
from entity.mouse import Mouse


class Paint:
    def __init__(self, width, height, name="Paint"):
        self.__init_glfw()

        # Atributos
        self.width = width
        self.height = height
        self.name = name

        # Window
        self.window = self.__init_window()
        glfw.make_context_current(self.window)

        # Pixel, Drawer e Mouse
        self.pixels = np.zeros((height, width, 3), dtype=np.uint8)
        self.drawer = Drawer(self.pixels)
        self.mouse = Mouse(self.window)

    def __init_glfw(self):
        if not glfw.init():
            raise Exception("Could not initialize glfw")

    def __init_window(self):
        window = glfw.create_window(self.width, self.height, self.name, None, None)

        if not window:
            glfw.terminate()
            raise Exception("Window not created")
        return window

    def is_window_closed(self):
        return glfw.window_should_close(self.window)

    def get_drawer(self):
        return self.drawer

    def get_mouse(self):
        return self.mouse

    def update_frame(self):
        glDrawPixels(self.width, self.height, GL_RGB, GL_UNSIGNED_BYTE, np.flipud(self.pixels))
        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def background_color(self, color):
        self.pixels[:] = color

    def new_canvas(self):
        self.background_color(WHITE)

    def save(self, filename="desenho.ppm"):
        canvas = self.pixels[0:CANVAS_HEIGHT, TOOLBAR_WIDTH:TOOLBAR_WIDTH + CANVAS_WIDTH]
        header = f"P6\n{CANVAS_WIDTH} {CANVAS_HEIGHT}\n255\n".encode()

        with open(filename, "wb") as file:
            file.write(header)
            file.write(canvas.tobytes())




