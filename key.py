key = ""
mouse_button = 0
mouse_x, mouse_y = 0, 0

right = False
left = False
up = False
down = False

koff = False


def press(e):
    global key, right, left, up, down, koff
    key = e.keysym
    if key == "Up":
        up = True
    if key == "Down":
        down = True
    if key == "Left":
        left = True
    if key == "Right":
        right = True
    koff = True


def release(e):
    global key, right, left, up, down, koff
    key = e.keysym
    if key == "Up":
        up = False
    if key == "Down":
        down = False
    if key == "Left":
        left = False
    if key == "Right":
        right = False
    key = ""
    koff = False


def mouse(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y


def mouse_click(e):
    global mouse_button
    if mouse_button == 0:
        mouse_button = e.num


def mouse_release(e):
    global mouse_button
    if mouse_button != 0:
        mouse_button = 0
