# BGM,効果音:魔王魂
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
from savedata import save, load

# ゲームの状態定数
state = 1  # 現在の状態
TITLE = 1
GAME_ENDLESS = 2
GAME_NORMAL = 3
CLEAR = 4
GAMEOVER = 5

gamemode = GAME_ENDLESS
timer = 0
frame_ms = 50
clear_timer = 100
score = 0
hiscore = 0
clear_flg = False
# プレイヤー、敵、アイテムインスタンス
neko = None
enemies_neko = []
items = []

# フォントの種類、サイズ
fnt0 = ("Times New Roman", 8)
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

# 操作方法(デフォルト:キーボード)
key_or_mouse = player.MOVE_KEY
key_enter = True


def init_player():
    # プレイヤーの初期化
    global neko, c_width, c_height
    neko = player.Player(c_width/2, c_height/2)


def init_enemy():
    # 敵の初期化
    global enemies_neko
    enemies_neko = []
    spawn_enemy(1, 0)


def spawn_enemy(num, time):
    # 敵スポーン
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
            x, y, random.randint(0, 4), time))


def init_items():
    # アイテム初期化
    global items
    items = []


def spawn_item(num):
    # アイテムスポーン
    global items
    items.append(item.Item(c_width, c_height))


def main():
    global score, hiscore, state, fnt1, fnt2, clear_timer, timer, frame_ms, neko, items, enemies_neko, spawn_enemy_se, spawn_item_se, delete_se, gameover_se, key_or_mouse, key_enter, gamemode, clear_flg
    # 経過時間 ミリ秒→秒に変換
    play_time = math.floor(timer * frame_ms / 1000)
    canvas.delete("SCREEN")
    # タイトル画面
    if state == TITLE:
        # タイトルテキスト
        canvas.create_text(c_width/2, c_height/2, text="ねこサバイバー",
                           fill="blue", font=fnt2, tag="SCREEN")
        canvas.create_text(c_width/2, c_height/2+60, text="Press Space to Start",
                           fill="black", font=fnt1, tag="SCREEN")
        if key_or_mouse == player.MOVE_KEY:  # 操作方法:キーボード時
            canvas.create_text(c_width/2, c_height/2+180, text="操作方法:キーボード",
                               fill="black", font=fnt1, tag="SCREEN")
        elif key_or_mouse == player.MOVE_MOUSE:  # 操作方法:マウス時
            canvas.create_text(c_width/2, c_height/2+180, text="操作方法:マウス",
                               fill="black", font=fnt1, tag="SCREEN")
        if gamemode == GAME_NORMAL:
            canvas.create_text(c_width/2, c_height/2+120, text="ゲームモード:ノーマル",
                               fill="black", font=fnt1, tag="SCREEN")
        elif gamemode == GAME_ENDLESS:
            canvas.create_text(c_width/2, c_height/2+120, text="ゲームモード:エンドレス",
                               fill="black", font=fnt1, tag="SCREEN")
        if clear_flg:
            canvas.create_text(10, c_height - 10 - img_hakase_resized.height, text="お主が真の\n「ねこサバイバー」じゃ！！",
                               fill="red", font=fnt0, anchor="sw", tag="SCREEN")
            canvas.create_image(10, c_height - 10, image=img_hakase,
                                anchor="sw", tag="SCREEN")
        # 操作方法の変更
        if key.key == "a":
            key_or_mouse = player.MOVE_KEY
        if key.key == "s":
            key_or_mouse = player.MOVE_MOUSE

        # ゲームモードの変更
        if key.key == "Left":
            gamemode = GAME_ENDLESS
        if key.key == "Right":
            gamemode = GAME_NORMAL

        if hiscore != 0:  # 最長の生存時間表示
            canvas.create_text(10, 10, text=f"エンドレス生存時間:{hiscore}秒",
                               fill="red", font=fnt1, anchor="nw", tag="SCREEN")
        # spaceキーでゲームスタート
        if key.key == "space":
            init_player()
            init_enemy()
            init_items()
            state = gamemode
            print(state)
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
    if state == GAME_ENDLESS or state == GAME_NORMAL:
        # 経過時間表示
        if state == GAME_ENDLESS:
            canvas.create_text(10, 10, text=f"生存時間:{play_time}",
                               fill="black", font=fnt1, tag="SCREEN", anchor="nw")
        elif state == GAME_NORMAL:
            canvas.create_text(10, 10, text=f"クリアまで:{clear_timer - play_time}",
                               fill="black", font=fnt1, tag="SCREEN", anchor="nw")
        # 自機の座標移動、描画
        neko.move(c_width, c_height, key_or_mouse)
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
        if timer != 0 and timer*frame_ms % 5000 == 0:
            spawn_enemy(2, play_time)
            spawn_enemy_se.play()
            # 50%の確率でアイテム出現
            item_random = random.randrange(2)
            if item_random == 0:
                spawn_item(1)
                spawn_item_se.play()
        # 敵の座標移動、描画
        for enemy_neko in enemies_neko:
            enemy_neko.move(neko, play_time)
            canvas.create_image(
                enemy_neko.x, enemy_neko.y, image=img_enemy[enemy_neko.img_index], tag="SCREEN")
            # プレイヤーとの接触判定
            if enemy_neko.hit_check(neko):
                gameover_se.play()
                state = GAMEOVER
                score = play_time
                timer = 0
        timer += 1
        # ノーマルモードでクリア
        if gamemode == GAME_NORMAL and clear_timer - play_time <= 0:
            state = CLEAR
            score = play_time
            clear_flg = True
            timer = 0
    if state == GAMEOVER:
        if hiscore < score:
            hiscore = score
            save(hiscore)
        if gamemode == GAME_ENDLESS:
            canvas.create_text(10, 10, text=f"生存時間:{score}",
                               fill="black", font=fnt1, tag="SCREEN", anchor="nw")
        elif gamemode == GAME_NORMAL:
            canvas.create_text(10, 10, text=f"残り時間:{clear_timer - score}",
                               fill="black", font=fnt1, tag="SCREEN", anchor="nw")
        # GAMEOVERテキストを上から画面真ん中に移動しながら描画
        text_height = timer*5 if timer*5 <= c_height/2 else c_height/2
        canvas.create_text(c_width/2, text_height, text="GAME OVER",
                           fill="red", font=fnt2, tag="SCREEN")
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.stop()
        if timer == 60:
            state = TITLE
            timer = 0
        timer += 1
    if state == CLEAR:
        text_height = timer*5 if timer*5 <= c_height/2 else c_height/2
        canvas.create_text(c_width/2, text_height, text="GAME CLEAR",
                           fill="red", font=fnt2, tag="SCREEN")
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.stop()
        if timer == 60:
            state = TITLE
            timer = 0
        timer += 1

    root.after(frame_ms, main)


# ウインドウ用意
root = tk.Tk()
root.title("ねこサバイバー")
root.bind("<KeyPress>", key.press)
root.bind("<KeyRelease>", key.release)
root.bind("<Motion>", key.mouse)
root.bind("<Button>", key.mouse_click)
root.bind("<ButtonRelease>", key.mouse_release)
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
img_hakase_open = Image.open("images/hakase4_laugh.png")
img_hakase_resized = img_hakase_open.resize((100, 100))
img_hakase = ImageTk.PhotoImage(img_hakase_resized)
savedata = load()
hiscore = savedata["生存時間"]
# ゲーム実行
main()
root.mainloop()
