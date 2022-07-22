import math


class Enemy:
    def __init__(self, x, y, img_index, time):
        self.x = x
        self.y = y
        self.speed = 2
        self.img_index = img_index
        self.time = time

    # プレイヤーに向かって移動する
    def move(self, target, time):
        # 自分と相手の座標の差からラジアンを求める
        r = math.atan2(target.y-self.y, target.x-self.x)
        # 座標の移動処理
        if self.img_index == 0:
            self.x += self.speed*math.cos(r)
            self.y += self.speed*math.sin(r)
        if self.img_index == 1:
            self.x += (self.speed+3)*math.cos(r)
            self.y += self.speed*math.sin(r)
        if self.img_index == 2:
            self.x += self.speed*math.cos(r)
            self.y += (self.speed+3)*math.sin(r)
        if self.img_index == 3:
            self.x += (self.speed+3)*math.cos(r)
            self.y += (self.speed+3)*math.sin(r)
        if self.img_index == 4:
            self.x += (self.speed+5)*math.cos(r)
            self.y += (self.speed+5)*math.sin(r)
        # self.x += self.speed*math.cos(r)
        # self.y += self.speed*math.sin(r)

    # プレイヤーとの当たり判定
    def hit_check(self, target):
        if (self.x-target.x)**2 + (self.y-target.y)**2 < 52**2:
            return True
        return False
