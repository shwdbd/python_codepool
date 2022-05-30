#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HelloWorld2.py
@Time    :   2020/02/04 22:32:53
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   HelloWorld使用Application方式实现

有一个窗口框，一个供输入姓名的输入框和一个按钮。按钮按下后会弹出窗口回显"Hello, xxx"

'''
import tkinter as tk
import tkinter.messagebox as msg


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        # print(self.master.config())
        self.master.geometry('500x300+500+200')

    def create_widgets(self):
        # 姓名:
        self.l_name = tk.Label(self, text='请输入您的姓名：', width=30, height=2)
        self.l_name.grid(row=1, column=1)
        self.e_name = tk.Entry(self)
        self.e_name.grid(row=1, column=2)

        # 按钮
        self.btn_hello = tk.Button(
            self, text='打招呼', width=10, height=1, command=self.btn_hello_click)
        self.btn_hello.grid(row=2, column=1)
        self.btn_close = tk.Button(
            self, text='关闭', width=10, height=1, command=self.btn_close_click)
        self.btn_close.grid(row=2, column=2)

    def btn_hello_click(self):
        name = self.e_name.get()
        if name == '':
            msg.showwarning(title='Hi', message='请输入姓名')
            self.e_name.focus_set()
        else:
            msg.showinfo(title='Hi', message='Hello World，{0}'.format(name))

    def btn_close_click(self):
        self.master.destroy()


def show():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    show()
