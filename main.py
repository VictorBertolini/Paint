from buttons.action_button import ActionButton
from buttons.color_button import ColorButton
from buttons.thickness_button import ThicknessButton
from buttons.tool_button import ToolButton
from constants import WHITE, WIDTH, HEIGHT, RED, BLACK, GREEN, BLUE, YELLOW, ORANGE, PURPLE, TOOLBAR_WIDTH
from entity.paint import Paint
from entity.state import State
from tools.utils.bucket import Bucket
from tools.utils.circle import Circle
from tools.utils.eraser import Eraser
from tools.utils.filled_circle import FilledCircle
from tools.utils.filled_rectangle import FilledRectangle
from tools.utils.line import Line
from tools.utils.pencil import Pencil
from tools.toolbar import Toolbar
from tools.utils.rectangle import Rectangle

paint = Paint(WIDTH, HEIGHT)
drawer = paint.get_drawer()
mouse = paint.get_mouse()

paint.background_color(WHITE)
state = State()
toolbar = Toolbar(state)

paint.new_canvas()

tools = [Pencil(), Eraser(), Line(), Rectangle(), FilledRectangle(), Circle(), FilledCircle(), Bucket()]
state.tool = tools[0]

# Ferramentas
toolbar.add(ToolButton(25, 25, 50, 50, Pencil()))
toolbar.add(ToolButton(85, 25, 50, 50, Eraser()))
toolbar.add(ToolButton(25, 85, 50, 50, Line()))
toolbar.add(ToolButton(85, 85, 50, 50, Rectangle()))
toolbar.add(ToolButton(25, 145, 50, 50, FilledRectangle()))
toolbar.add(ToolButton(85, 145, 50, 50, Circle()))
toolbar.add(ToolButton(25, 205, 50, 50, FilledCircle()))
toolbar.add(ToolButton(85, 205, 50, 50, Bucket()))

# Espessura
toolbar.add(ThicknessButton(25, 285, 30, 30, 1))
toolbar.add(ThicknessButton(65, 285, 30, 30, 3))
toolbar.add(ThicknessButton(105, 285, 30, 30, 5))

# Cores
toolbar.add(ColorButton(25, 345, 30, 30, BLACK))
toolbar.add(ColorButton(65, 345, 30, 30, WHITE))
toolbar.add(ColorButton(25, 385, 30, 30, RED))
toolbar.add(ColorButton(65, 385, 30, 30, GREEN))
toolbar.add(ColorButton(25, 425, 30, 30, BLUE))
toolbar.add(ColorButton(65, 425, 30, 30, YELLOW))
toolbar.add(ColorButton(25, 465, 30, 30, ORANGE))
toolbar.add(ColorButton(65, 465, 30, 30, PURPLE))

# Ações
toolbar.add(ActionButton(25, HEIGHT - 75, 50, 50, paint.new_canvas))
toolbar.add(ActionButton(85, HEIGHT - 75, 50, 50, paint.save))

drawing = False

while not paint.is_window_closed():
    mouse.update()
    x, y = mouse.position()

    # Se mouse for pressionado
    if mouse.just_pressed():
        if x < TOOLBAR_WIDTH:
            toolbar.click(x, y)
        else:
            drawing = True
            state.tool.press(drawer, state, x, y)

    # Se mouse está sendo pressionado e no Canvas
    elif mouse.pressed() and drawing:
        state.tool.drag(drawer, state, x, y)

    # Se parou de apertar o mouse
    elif mouse.just_released():
        if drawing:
            state.tool.release(drawer, state, x, y)
        drawing = False

    toolbar.draw(drawer)
    paint.update_frame()

