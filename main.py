import tkinter as tk
import random
import key

# ゲームの状態定数
STATE = 0  # 現在の状態
TITLE = 1
GAME = 2
CLEAR = 3
GAMEOVER = 4

timer = 0
score = 0


def main():
    if key.up:
        print(key.up)
    root.after(50, main)


root = tk.Tk()
root.title("ハック＆スラッシュ")
root.bind("<KeyPress>", key.press)
root.bind("<KeyRelease>", key.release)
canvas = tk.Canvas(width=600, height=400)
canvas.pack()
main()
root.mainloop()
