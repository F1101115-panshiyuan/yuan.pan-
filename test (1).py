#15165145165
#
import tkinter as tk # 匯入 tkinter 並命名為 tk
win =tk.Tk() # 建立主視窗物件
win.geometry("400x400") #設定視窗大小為 400*400 像素
win.title("視窗模式") #設定視窗標題




win.mainloop() #啟動主事件迴路
import tkinter as tk
from tkinter import ttk

def main():
    # 建立主視窗
    root = tk.Tk()
    root.title("Tkinter 範例視窗")
    root.geometry("400x200")   # 設定視窗大小

    # 標籤
    label = ttk.Label(root, text="Hello Tkinter!", font=("Arial", 16))
    label.pack(pady=20)

    # 按鈕
    def on_click():
        label.config(text="買！")

    button = ttk.Button(root, text="點我", command=on_click)
    button.pack()

    # 主事件迴圈
    root.mainloop()

if __name__ == "__main__":
    main()
