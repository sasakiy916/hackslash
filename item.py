import random


class Item:
    # コンストラクタ
    def __init__(self, c_width, c_height):
        self.size = 80
        self.x = random.randint(self.size, c_width-self.size)
        self.y = random.randint(self.size, c_height-self.size)

    # プレイヤーとの当たり判定
    def hit_check(self, target):
        if (self.x-target.x)**2 + (self.y-target.y)**2 < (self.size/2)**2:
            return True
        return False
