#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HelloWorld.py
@Time    :   2020/02/04 16:56:33
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   第一个Tkinter程序

有一个窗口框，一个供输入姓名的输入框和一个按钮。按钮按下后会弹出窗口回显"Hello, xxx"

'''
import tkinter as tk
import tkinter.messagebox as msg


def show():
    window = tk.Tk()
    window.title('Hello World')
    window.geometry('500x300')

    # 姓名提示框
    l_name = tk.Label(window, text='请输入您的姓名', bg='green',
                      font=('Arial', 12), width=30, height=2)
    l_name.pack()

    # 姓名输入框
    e_name = tk.Entry(window, font=('Arial', 14))
    e_name.pack()

    # Say Hi 动作按钮
    btn_hello = tk.Button(window, text='打招呼', font=(
        'Arial', 12), width=10, height=1, command=lambda: btn_hello_click(e_name))
    btn_hello.pack()

    # 关闭按钮
    btn_close = tk.Button(window, text='关闭', width=10,
                          height=1, command=lambda: btn_close_click(window))
    btn_close.pack()

    window.mainloop()


def btn_close_click(win):
    win.destroy()


def btn_hello_click(e_name):
    name = e_name.get()
    if name == '':
        msg.showwarning(title='Hi', message='请输入姓名')
        e_name.focus_set()
    else:
        msg.showinfo(title='Hi', message='Hello World，{0}'.format(name))
    # print('click me ' + name)


if __name__ == "__main__":
    show()
