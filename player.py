import key


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10

    def move(self):
        if key.right:
            self.x += self.speed
        if key.left:
            self.x -= self.speed
        if key.up:
            self.y -= self.speed
        if key.down:
            self.y += self.speed
