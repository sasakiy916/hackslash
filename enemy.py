import math


class Enemy:
    def __init__(self, x, y, img_index):
        self.x = x
        self.y = y
        self.speed = 5
        self.img_index = img_index

    # プレイヤーに向かって移動する
    def move(self, target):
        # 自分と相手の座標の差からラジアンを求める
        r = math.atan2(target.y-self.y, target.x-self.x)
        # 座標の移動処理
        self.x += self.speed*math.cos(r)
        self.y += self.speed*math.sin(r)

    # プレイヤーとの当たり判定
    def hit_check(self, target):
        if (self.x-target.x)**2 + (self.y-target.y)**2 < 64**2:
            return True
        return False
