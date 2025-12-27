import tkinter as tk
import random
import time

# =============================
# 接水球小遊戲【第三版｜高級版】
# 功能：
# 1. 開始畫面
# 2. 60 秒計時
# 3. 闖關制（5 關）
# 4. 失誤扣分
# 5. 結束總結畫面
# =============================

WIDTH = 440
HEIGHT = 560
GAME_TIME = 60
MAX_LEVEL = 5

root = tk.Tk()
root.title("💦 接水球大挑戰 💦")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#E1F5FE")
canvas.pack()

# -------- 遊戲狀態 --------
score = 0
level = 1
start_time = None
ball_speed = 3
playing = False

# -------- UI 元件 --------
score_text = canvas.create_text(70, 20, text="分數：0", font=("Arial", 14))
level_text = canvas.create_text(220, 20, text="關卡：1", font=("Arial", 14))
time_text = canvas.create_text(360, 20, text="時間：60", font=("Arial", 14))

# -------- 籃子 --------
basket_width = 90
basket_height = 18
basket_y = HEIGHT - 40
basket = canvas.create_rectangle(
    WIDTH//2 - basket_width//2,
    basket_y - basket_height//2,
    WIDTH//2 + basket_width//2,
    basket_y + basket_height//2,
    fill="#0277BD", outline=""
)

# -------- 水球 --------
ball_radius = 12
ball = canvas.create_oval(0, 0, 0, 0, fill="#4FC3F7", outline="")

# -------- 開始畫面 --------
start_text = canvas.create_text(
    WIDTH//2, HEIGHT//2 - 40,
    text="💦 接水球大挑戰 💦\n\n← → 移動籃子\n接到水球得分\n掉地扣分\n\n按【空白鍵】開始",
    font=("Arial", 18), fill="#01579B"
)

# -------- 控制 --------

def move_left(event):
    if not playing: return
    canvas.move(basket, -30, 0)
    x1, _, x2, _ = canvas.coords(basket)
    if x1 < 0:
        canvas.move(basket, -x1, 0)


def move_right(event):
    if not playing: return
    canvas.move(basket, 30, 0)
    x1, _, x2, _ = canvas.coords(basket)
    if x2 > WIDTH:
        canvas.move(basket, WIDTH - x2, 0)


def start_game(event=None):
    global playing, start_time, score, level, ball_speed
    playing = True
    start_time = time.time()
    score = 0
    level = 1
    ball_speed = 3
    canvas.delete(start_text)
    canvas.itemconfig(score_text, text="分數：0")
    canvas.itemconfig(level_text, text="關卡：1")
    reset_ball()
    update_game()


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", start_game)

# -------- 重設水球 --------

def reset_ball():
    x = random.randint(20, WIDTH - 20)
    canvas.coords(
        ball,
        x - ball_radius, 0,
        x + ball_radius, ball_radius * 2
    )

# -------- 關卡判定 --------

def check_level():
    global level, ball_speed
    if score >= level * 5 and level < MAX_LEVEL:
        level += 1
        ball_speed += 1.2
        canvas.itemconfig(level_text, text=f"關卡：{level}")

# -------- 遊戲更新 --------

def update_game():
    global score
    if not playing:
        return

    elapsed = int(time.time() - start_time)
    remain = GAME_TIME - elapsed

    if remain <= 0:
        end_game()
        return

    canvas.itemconfig(time_text, text=f"時間：{remain}")

    canvas.move(ball, 0, ball_speed)

    bx1, by1, bx2, by2 = canvas.coords(basket)
    fx1, fy1, fx2, fy2 = canvas.coords(ball)

    # 接到水球
    if fy2 >= by1 and fx2 >= bx1 and fx1 <= bx2:
        score += 1
        canvas.itemconfig(score_text, text=f"分數：{score}")
        check_level()
        reset_ball()

    # 掉地扣分
    if fy1 > HEIGHT:
        score = max(0, score - 1)
        canvas.itemconfig(score_text, text=f"分數：{score}")
        reset_ball()

    root.after(30, update_game)

# -------- 結束畫面 --------

def end_game():
    global playing
    playing = False
    canvas.create_text(
        WIDTH//2, HEIGHT//2,
        text=f"🎉 遊戲結束 🎉\n\n最終分數：{score}\n達到關卡：{level}\n\n按【空白鍵】再玩一次",
        font=("Arial", 20), fill="#01579B"
    )


root.mainloop()