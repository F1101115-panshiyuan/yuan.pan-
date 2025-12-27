import tkinter as tk
import random
import time

# =====================
# 接水球小遊戲（國小升級版）
# 功能：60 秒計時、速度遞增、水球主題
# =====================

root = tk.Tk()
root.title("💦 接水球小遊戲 💦")
root.resizable(False, False)

WIDTH = 420
HEIGHT = 520
GAME_TIME = 60  # 遊戲秒數

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#E0F7FA")
canvas.pack()

# ---------- 狀態 ----------
score = 0
start_time = time.time()
fruit_speed = 3

time_text = canvas.create_text(330, 20, text="時間：60", font=("Arial", 14))
score_text = canvas.create_text(70, 20, text="分數：0", font=("Arial", 14))

# ---------- 籃子 ----------
basket_width = 90
basket_height = 18
basket_y = HEIGHT - 35
basket = canvas.create_rectangle(
    WIDTH//2 - basket_width//2,
    basket_y - basket_height//2,
    WIDTH//2 + basket_width//2,
    basket_y + basket_height//2,
    fill="#0288D1",
    outline=""
)

# ---------- 水球 ----------
ball_radius = 12
ball_x = random.randint(20, WIDTH - 20)
ball_y = 0
ball = canvas.create_oval(
    ball_x - ball_radius,
    ball_y - ball_radius,
    ball_x + ball_radius,
    ball_y + ball_radius,
    fill="#4FC3F7",
    outline=""
)

# ---------- 控制 ----------

def move_left(event):
    canvas.move(basket, -25, 0)
    x1, _, x2, _ = canvas.coords(basket)
    if x1 < 0:
        canvas.move(basket, -x1, 0)


def move_right(event):
    canvas.move(basket, 25, 0)
    x1, _, x2, _ = canvas.coords(basket)
    if x2 > WIDTH:
        canvas.move(basket, WIDTH - x2, 0)


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# ---------- 重設水球 ----------

def reset_ball():
    global ball_x, ball_y
    ball_x = random.randint(20, WIDTH - 20)
    ball_y = 0
    canvas.coords(
        ball,
        ball_x - ball_radius,
        ball_y - ball_radius,
        ball_x + ball_radius,
        ball_y + ball_radius,
    )

# ---------- 遊戲更新 ----------

def update_game():
    global ball_y, score, fruit_speed

    # 計時
    elapsed = int(time.time() - start_time)
    remain = GAME_TIME - elapsed

    if remain <= 0:
        canvas.create_text(
            WIDTH//2, HEIGHT//2,
            text=f"🎉 遊戲結束！\n你的分數：{score}",
            font=("Arial", 22), fill="#01579B"
        )
        return

    canvas.itemconfig(time_text, text=f"時間：{remain}")

    # 水球移動
    ball_y += fruit_speed
    canvas.move(ball, 0, fruit_speed)

    bx1, by1, bx2, by2 = canvas.coords(basket)
    fx1, fy1, fx2, fy2 = canvas.coords(ball)

    # 接到水球
    if fy2 >= by1 and fx2 >= bx1 and fx1 <= bx2:
        score += 1
        fruit_speed += 0.2  # 越來越快
        canvas.itemconfig(score_text, text=f"分數：{score}")
        reset_ball()

    # 掉出畫面
    if ball_y > HEIGHT:
        reset_ball()

    root.after(30, update_game)


update_game()
root.mainloop()