#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   HelloWorld.py
@Time    :   2020/02/07 10:04:33
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   第一个Pyqt5程序

有一个窗口框，一个供输入姓名的输入框和一个按钮。按钮按下后会弹出窗口回显"Hello, xxx"

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QIcon


class HelloWorldWin(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.btn = QPushButton('Dialog', self)
        # self.btn.move(20, 20)
        # self.btn.clicked.connect(self.showDialog)

        self.le_name = QLineEdit(self, text='请输入姓名')
        self.le_name.move(130, 22)


        self.setGeometry(500, 300, 500, 220)
        # 窗口title和Icon
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))



        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = HelloWorldWin()
    sys.exit(app.exec_())
