import math


class Enemy:
    def __init__(self, x, y, img_index, time):
        self.x = x  # x座標
        self.y = y  # y座標
        self.speed = 2  # 足の速さ
        self.img_index = img_index  # 画像番号
        self.time = time  # 出現時の経過時間

    def move(self, target, time):
        # 自分と相手の座標の差からラジアンを求める
        r = math.atan2(target.y-self.y, target.x-self.x)
        # 座標の移動処理(キャラの種類で動きが変わる)
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
            # 5秒毎に1秒加速
            is_quick = (time - self.time) % 5 == 0
            speed = 0
            if is_quick:
                speed = 10
            elif not(is_quick):
                speed = 0
            self.x += (self.speed+speed)*math.cos(r)
            self.y += (self.speed+speed)*math.sin(r)
        # self.x += self.speed*math.cos(r)        # self.x += self.speed*math.cos(r)            self.y += (self.speed+speed)*math.sin(r)

        # self.x += self.speed*math.cos(r)        # self.x += self.speed*math.cos(r)        # self.y += self.speed*math.sin(r)

    # プレイヤーとの当たり判定
    def hit_check(self, target):
        if (self.x-target.x)**2 + (self.y-target.y)**2 < 52**2:
            return True
        return False
