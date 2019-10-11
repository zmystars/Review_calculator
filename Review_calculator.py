# -*- coding: utf-8 -*-
"""
程序名称：简易计算器（GUI界面）
题目要求：
1.使用GUI界面，需有0~9和.键、加减乘除（+-*/）键、Cls键（清除）
2.input区块可用鼠标输入，也可用键盘输入
3.容许错误输入，输出错误信息“Infinity”。（例如输入“10/0”，输出“Infinity”）
"""

def btn(root, text, row, col, w, colspan, command):
    button = tk.Button(root, text=text, width=w, command=command)
    button.grid(row=row, column=col, padx=5, pady=5, columnspan=colspan)

def get_input(argu):
    entry.insert("end", argu) # 将按钮文字输入entry组件

def calc():
    try:
        input = entry.get() # 获取entry组件输入的内容
        output = eval(input) # 获取运算结果
        entry.delete(0, "end") # 清除entry组件输入的内容
        label.config(text = output) # 在label组件显示文字
    except:
        label.config(text = "Infinity") # 在label组件显示错误信息

def clear():
    entry.delete(0, "end")
    label.config(text = "")

import tkinter as tk
win = tk.Tk()
win.title("简易计算器")

frame = tk.Frame(win)
frame.pack()
frame1 = tk.Frame(win)
frame1.pack()

entry = tk.Entry(frame, bg="#ffccff", borderwidth=3)
entry.pack(fill="x")
label = tk.Label(frame, bg="#ffffcc", anchor="e", text="计算结果")
label.pack(fill="x")

key = ["123+", "456-", "789*", "0./"]
for x_index, x in enumerate(key):
    for y_index, y in enumerate(x):
        btn(frame1, y, x_index, y_index, 6, 1, command=(lambda y=y : get_input(y)))

btn(frame1, "Cls", 3, 3, 6, 1, command=clear)
btn(frame1, "=", 5, 0, 20, 4, command=calc)

win.mainloop()
