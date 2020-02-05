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
        print(self.config())
        # self['geometry'] = '500x300'

    def create_widgets(self):
        # 姓名提示框
        self.l_name = tk.Label(self)
        self.l_name['text'] = '请输入您的姓名'
        self.l_name['bg'] = 'green'
        self.l_name['width'] = 3
        self.l_name['height'] = 2
        self.l_name['font'] = ('Arial', 12)
        # self.l_name = tk.Label(window, text='请输入您的姓名', bg='green',
        #               font=('Arial', 12), width=30, height=2)
        self.l_name.pack()


def show():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    show()