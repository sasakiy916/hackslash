from pickle import NONE
import tkinter as tk
import random
import key
import player
import enemy
from PIL import Image, ImageTk

# ゲームの状態定数
state = 1  # 現在の状態
TITLE = 1
GAME = 2
CLEAR = 3
GAMEOVER = 4

timer = 0
score = 0
neko = None
enemy_neko = []

fnt1 = ("Times New Roman", 24)
c_width = 600
c_height = 400


def init_player():
    global neko, c_width, c_height
    neko = player.Player(c_width/2, c_height/2)


def init_enemy():
    num = 1
    for i in range(num):
        enemy_neko.append(enemy.Enemy(
            random.randint(0, c_width), random.randint(0, 10)))


def main():
    global state, fnt1
    canvas.delete("SCREEN")
    if state == TITLE:
        canvas.create_text(c_width/2, c_height/2, text="ねこサバイバー",
                           fill="gold", font=fnt1, tag="SCREEN")
        if key.key == "space":
            init_player()
            init_enemy()
            state = GAME
    if state == GAME:
        # キャラの座標移動
        neko.move()
        enemy_neko[0].move(neko)
        # キャラの描画
        canvas.create_image(neko.x, neko.y, image=img_player, tag="SCREEN")
        canvas.create_image(
            enemy_neko[0].x, enemy_neko[0].y, image=img_enemy[2], tag="SCREEN")
    root.after(50, main)


root = tk.Tk()
root.title("ねこサバイバー")
root.bind("<KeyPress>", key.press)
root.bind("<KeyRelease>", key.release)
canvas = tk.Canvas(width=c_width, height=c_height)
canvas.pack()
# 画像読み込み
img = Image.open("images/neko1.png")
img_player = ImageTk.PhotoImage(img)
img_bullet = tk.PhotoImage(file="images/neko_niku.png")
img_enemy = [
    tk.PhotoImage(file="images/neko2.png"),
    tk.PhotoImage(file="images/neko3.png"),
    tk.PhotoImage(file="images/neko4.png"),
    tk.PhotoImage(file="images/neko5.png"),
    tk.PhotoImage(file="images/neko6.png"),
]

main()
root.mainloop()
