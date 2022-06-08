import threading
import time

exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, delay, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.delay, self.counter)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1, 2)
thread2 = myThread(2, "Thread-2", 1, 3)

# # 开启新线程
thread1.start()
# thread2.start()

print('============')
total_count = 3
while total_count > 0:
    # # 开启新线程
    # thread1.run()
    # thread2.run()
    # 等待
    
    if not thread1.isAlive():
        thread1.run()
    else:
        thread1.join()
    # if not thread2.isAlive():
    #     thread2.run()

    # thread1.join()
    # thread2.join()

    print('-----------------')
    time.sleep(10)
    total_count = total_count - 1


print("退出主线程")