import tkinter as tk
import random
import math
from PIL import Image, ImageTk
import pygame
# 自作モジュール
import key
import player
import enemy
import item

# ゲームの状態定数
state = 1  # 現在の状態
TITLE = 1
GAME = 2
CLEAR = 3
GAMEOVER = 4

timer = 0
timer_count = 50
score = 0
# プレイヤー、敵、アイテムインスタンス
neko = None
enemies_neko = []
items = []

# フォントの種類、サイズ
fnt1 = ("Times New Roman", 24)
fnt2 = ("Times New Roman", 40)
# キャンバスの大きさ
c_width = 600
c_height = 400

# 効果音
spawn_item_se = None
spawn_enemy_se = None
delete_se = None
gameover_se = None


def init_player():
    global neko, c_width, c_height
    neko = player.Player(c_width/2, c_height/2)


def init_enemy():
    global enemies_neko
    enemies_neko = []
    spawn_enemy(1)


def spawn_enemy(num):
    global enemies_neko
    for i in range(num):
        # 出現方向(上下左右)、場所抽選
        dir = random.randint(1, 4)
        if dir == 1:  # 上
            x = random.randint(0, c_width)
            y = -80
        if dir == 2:  # 下
            x = random.randint(0, c_width)
            y = c_height+80
        if dir == 3:  # 左
            x = -80
            y = random.randint(0, c_height)
        if dir == 4:  # 右
            x = c_width + 80
            y = random.randint(0, c_height)
        # 敵をインスタンス化
        enemies_neko.append(enemy.Enemy(
            x, y, random.randint(0, 4)))


def spawn_item(num):
    global items
    items.append(item.Item(c_width, c_height))


def main():
    global state, fnt1, fnt2, timer, timer_count, neko, items, enemies_neko, spawn_enemy_se, spawn_item_se, delete_se, gameover_se
    # 経過時間 ミリ秒→秒に変換
    play_time = math.floor(timer * timer_count / 1000)
    canvas.delete("SCREEN")
    if state == TITLE:
        # タイトル画面テキスト
        canvas.create_text(c_width/2, c_height/2, text="ねこサバイバー",
                           fill="blue", font=fnt2, tag="SCREEN")
        canvas.create_text(c_width/2, c_height/2+80, text="Press Space to Start",
                           fill="gold", font=fnt1, tag="SCREEN")
        # spaceキーでゲームスタート
        if key.key == "space":
            init_player()
            init_enemy()
            state = GAME
            pygame.init()
            # 音声読み込み
            try:
                pygame.mixer.music.load("sound/main.mp3")
                pygame.mixer.music.set_volume(0.2)
                spawn_enemy_se = pygame.mixer.Sound("sound/nyan.mp3")
                spawn_item_se = pygame.mixer.Sound("sound/item.mp3")
                delete_se = pygame.mixer.Sound("sound/delete.mp3")
                gameover_se = pygame.mixer.Sound("sound/gameover.mp3")
            except:
                print("音声読み込み失敗")
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play(-1)
            canvas.create_text(10, 10, text=f"TIME:0",
                               fill="black", font=fnt1, tag="SCREEN", anchor="nw")
    if state == GAME:
        # 経過時間表示
        canvas.create_text(10, 10, text=f"TIME:{play_time}",
                           fill="black", font=fnt1, tag="SCREEN", anchor="nw")
        # 自機の座標移動、描画
        neko.move(c_width, c_height)
        canvas.create_image(neko.x, neko.y, image=img_player, tag="SCREEN")
        # アイテムの描画
        for item in items:
            canvas.create_image(item.x, item.y, image=img_item, tag="SCREEN")
            # アイテムに取得で敵を全部消す
            if item.hit_check(neko):
                enemies_neko = []
                items.remove(item)
                delete_se.play()
        # 5秒毎に敵を追加
        if timer*timer_count % 5000 == 0:
            spawn_enemy(2)
            spawn_enemy_se.play()
            # 50%の確率でアイテム出現
            item_random = random.randrange(2)
            if item_random == 0:
                spawn_item(1)
                spawn_item_se.play()
        # 敵の座標移動、描画
        for enemy_neko in enemies_neko:
            enemy_neko.move(neko)
            canvas.create_image(
                enemy_neko.x, enemy_neko.y, image=img_enemy[enemy_neko.img_index], tag="SCREEN")
            # プレイヤーとの接触判定
            if enemy_neko.hit_check(neko):
                gameover_se.play()
                state = GAMEOVER
                timer = 0
    if state == GAMEOVER:
        canvas.create_text(c_width/2, c_height/2, text="GAME OVER",
                           fill="red", font=fnt2, tag="SCREEN")
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.stop()
        if timer == 30:
            state = TITLE
            timer = 0
    timer += 1
    root.after(timer_count, main)


# ウインドウ用意
root = tk.Tk()
root.title("ねこサバイバー")
root.bind("<KeyPress>", key.press)
root.bind("<KeyRelease>", key.release)
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()
# 画像読み込み
img_player_open = Image.open("images/neko1.png")
img_player = ImageTk.PhotoImage(img_player_open)
img_item = Image.open("images/neko_niku.png")
img_item = ImageTk.PhotoImage(img_item)
img_enemy_open = [
    Image.open("images/neko2.png"),
    Image.open("images/neko3.png"),
    Image.open("images/neko4.png"),
    Image.open("images/neko5.png"),
    Image.open("images/neko6.png"),
]
img_enemy = []
for img in img_enemy_open:
    img_enemy.append(ImageTk.PhotoImage(img))

# ゲーム実行
main()
root.mainloop()
