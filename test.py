import tkinter as tk
import random

# 建立視窗
root = tk.Tk()
root.title("🍎 接水果小遊戲 🍌")
root.resizable(False, False)

WIDTH = 400
HEIGHT = 500

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#f0f8ff")
canvas.pack()

# 分數
score = 0
score_text = canvas.create_text(70, 20, text="分數：0", font=("Arial", 14))

# 籃子
basket_width = 80
basket_height = 15
basket_x = WIDTH // 2
basket_y = HEIGHT - 30
basket = canvas.create_rectangle(
    basket_x - basket_width // 2,
    basket_y - basket_height // 2,
    basket_x + basket_width // 2,
    basket_y + basket_height // 2,
    fill="#8B4513"
)

# 水果
fruit_radius = 10
fruit_x = random.randint(20, WIDTH - 20)
fruit_y = 0
fruit_speed = 4
fruit = canvas.create_oval(
    fruit_x - fruit_radius,
    fruit_y - fruit_radius,
    fruit_x + fruit_radius,
    fruit_y + fruit_radius,
    fill="red"
)

# 移動籃子

def move_left(event):
    canvas.move(basket, -20, 0)
    x1, _, x2, _ = canvas.coords(basket)
    if x1 < 0:
        canvas.move(basket, -x1, 0)


def move_right(event):
    canvas.move(basket, 20, 0)
    x1, _, x2, _ = canvas.coords(basket)
    if x2 > WIDTH:
        canvas.move(basket, WIDTH - x2, 0)


root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# 重設水果

def reset_fruit():
    global fruit_x, fruit_y
    fruit_x = random.randint(20, WIDTH - 20)
    fruit_y = 0
    canvas.coords(
        fruit,
        fruit_x - fruit_radius,
        fruit_y - fruit_radius,
        fruit_x + fruit_radius,
        fruit_y + fruit_radius,
    )


# 遊戲更新

def update_game():
    global fruit_y, score

    fruit_y += fruit_speed
    canvas.move(fruit, 0, fruit_speed)

    # 取得位置
    bx1, by1, bx2, by2 = canvas.coords(basket)
    fx1, fy1, fx2, fy2 = canvas.coords(fruit)

    # 碰撞判斷
    if fy2 >= by1 and fx2 >= bx1 and fx1 <= bx2:
        score += 1
        canvas.itemconfig(score_text, text=f"分數：{score}")
        reset_fruit()

    # 掉出畫面
    if fruit_y > HEIGHT:
        reset_fruit()

    root.after(30, update_game)


update_game()
root.mainloop()