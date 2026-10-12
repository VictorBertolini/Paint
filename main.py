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

for i, tool in enumerate(tools):
    x = 25 + (i % 2) * 60
    y = 25 + (i // 2) * 60
    toolbar.add(ToolButton(x, y, 50, 50, tool))

for i, thickness in enumerate([1, 3, 5]):
    toolbar.add(ThicknessButton(25 + i * 40, 285, 30, 30, thickness))

colors = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE]

for i, color in enumerate(colors):
    x = 25 + (i % 2) * 40
    y = 345 + (i // 2) * 40
    toolbar.add(ColorButton(x, y, 30, 30, color))

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

