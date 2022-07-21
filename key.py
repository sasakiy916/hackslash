key = ""

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
    koff = False
    key = ""
