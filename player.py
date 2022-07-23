import key
size = 36  # キャラの大きさ
MOVE_KEY = 0
MOVE_MOUSE = 1


class Player:
    # コンストラクタ
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    # 移動処理
    def move(self, c_width, c_height, operation=MOVE_KEY):
        global size
        if operation == MOVE_KEY:
            if key.right and self.x < c_width - size:  # 右
                self.x += self.speed
            if key.left and self.x > size:  # 左
                self.x -= self.speed
            if key.down and self.y < c_height - size:  # 下
                self.y += self.speed
            if key.up and self.y > size:  # 上
                self.y -= self.speed
        elif operation == MOVE_MOUSE:
            if self.x < c_width - size:  # 右
                self.x = key.mouse_x
            if self.x > size:  # 左
                self.x = key.mouse_x
            if self.y < c_height - size:  # 下
                self.y = key.mouse_y
            if self.y > size:  # 上
                self.y = key.mouse_y

    def move_mouse(self, c_width, c_height):
        global size
        if self.x < c_width - size:  # 右
            self.x = self.speed
        if self.x > size:  # 左
            self.x = self.speed
        if self.y < c_height - size:  # 下
            self.y = self.speed
        if self.y > size:  # 上
            self.y = self.speed
