#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2020/02/23 10:58:18
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   一个完整的可启动、可关闭的多线程服务器例子

- class: Server 服务器类
- Class: AbstractThread 抽象服务
- Class: ThreadA 服务实现A
- Class: ThreadB 服务实现B

开关：server.txt，里面如果是open则表示启动

'''
import threading
import time

CONFIG_FILE = r'src\wdbd\codepool\threads\server.txt'


class Server:
    """多线程服务器
    """

    def __init__(self):
        # 将设置
        pass

    def get_server_status(self):
        """返回服务器状态
        """
        with open(CONFIG_FILE, mode='r') as f:
            status = f.readline()
            return status

    def start(self):
        """启动总服务
        """
        print('【主线程】服务器启动... ')

        if self.get_server_status() != 'open':
            print('【主线程】服务器状态为 已有示例正在运行或正在关闭，为确保安全，本次服务启动终止！')
            return

        # 读取服务列表：
        threads_list = []
        implA = ThreadA('111')
        implB = ThreadB('111')
        t1 = AbstractThread('111', implA)
        t2 = AbstractThread('222', implB)
        threads_list.append(t1)
        threads_list.append(t2)
        print('【主线程】共有{0}个服务 ... '.format(len(threads_list)))

        # 开启新线程
        for t in threads_list:
            t.start()
        print('【主线程】服务启动完毕 ... ')

        # 轮询检查，是否应该关闭服务
        while True:
            if self.get_server_status() == 'close':     # 所有子线程都已关闭
                for t in threads_list:
                    t.stop()
                print('【主线程】所有子线程都已关闭')
                break
            else:
                print('【主线程】还有线程运行，继续等待')
                time.sleep(5)

        print('【主线程】服务器主线程关闭')


class AbstractThread(threading.Thread):
    """
    子线程基类
    线程启动(start)后，不再能关闭(close)，直到主线程调用t.close函数关闭
    """
    status = 'open'    # 当前线程的状态，open|close

    def __init__(self,  name, impl_obj, *args, **kwargs):
        super(AbstractThread, self).__init__(*args, **kwargs)
        self.name = name    # 线程名称
        self._stop_event = threading.Event()
        self.impl_obj = impl_obj
        self.status = 'open'

    def stop(self):
        # 主线程调用本线程，本线程应将关闭标识设置，提醒run函数关闭线程
        self.status = 'close'
        print('【线程 {0}】收到主线程发来的Stop线程的信号! '.format(self.name))

    def is_stop(self):
        # 判断是否线程应该终止？
        if self.status == 'close':
            return True
        else:
            return False

    def run(self):
        print("【线程 {0}】开始运行子线程 -- ".format(self.name))
        while True:
            # print("sleep 1s " + str(self.tid))
            self.impl_obj.do_biz()
            print("【线程 {0}】执行日间处理完成，等待3秒 ... ".format(self.name))
            time.sleep(3)
            if self.is_stop():
                # 做一些必要的收尾工作
                self.impl_obj.do_close()
                print("【线程 {0}】执行收尾完成，线程关闭".format(self.name))
                break


class ThreadA():

    def __init__(self, name):
        self.name = name
        super().__init__()

    def do_biz(self):
        print('【线程实例A {0}】 do something ... '.format(self.name))

    def do_close(self):
        print('【线程实例A {0}】 do something for close ... '.format(self.name))


class ThreadB():

    def __init__(self, name):
        self.name = name
        super().__init__()

    def do_biz(self):
        print('【线程实例B {0}】 do something ... '.format(self.name))

    def do_close(self):
        print('【线程实例B {0}】 do something for close ... '.format(self.name))


if __name__ == "__main__":
    srv = Server()
    # r = srv.get_server_status()
    # print(r)
    srv.start()
