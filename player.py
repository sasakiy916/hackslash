class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, key):
        if key == "":
            self.x += 1
