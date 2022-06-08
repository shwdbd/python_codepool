#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   download_unit.py
@Time    :   2021/04/16 09:54:15
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   数据下载多线程模拟
'''
from threading import Thread
from time import sleep, ctime
import os


class DLUnit(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('开始子进程{0}'.format(self.name))
        count = 0
        while count < 3:
            if self.ready():
                self.download()
            else:
                print("无法运行")
            sleep(2)
            count += 1
        print('结束子进程{0}'.format(self.name))

    def ready(self):
        # TODO 此处判断是否应该继续执行？
        return True

    def download(self):
        print("下载数据")


class UnitA(DLUnit):

    def ready(self):
        # TODO 此处判断是否应该继续执行？
        return True

    def download(self):
        print("下载数据{name}(pid={pid})".format(name=self.name, pid=os.getpid()))
        sleep(4)


class UnitB(DLUnit):

    def ready(self):
        return True

    def download(self):
        print("下载数据{name}(pid={pid})".format(name=self.name, pid=os.getpid()))
        sleep(2)


class DLServer:
    """数据下载服务器
    """

    def __init__(self):
        # 准备各类参数，读取各配置文件
        pass

    def start(self):
        # 初始化
        self.unit_list = [UnitA("A"), UnitB("B")]
        self.thead_pool = []

        for unit in self.unit_list:
            t = unit     # 启动线程
            # t.run()
            self.thead_pool.append(t)
            t.start()
        print("线程合计 = {0}".format(len(self.thead_pool)))
        print("等待 ... ")
        sleep(5)

        for t in self.thead_pool:
            t.join()
        print("服务终止！")

    def shutdown(self):
        # 线程关闭
        for t in self.thead_pool:
            t.stop()
        print("线程合计 = {0}".format(len(self.thead_pool)))
        print("服务结束")


if __name__ == "__main__":
    server = DLServer()
    server.start()
    # sleep(5)
    # server.shutdown()
    # a = UnitA("a")