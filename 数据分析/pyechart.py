import threading
import time
import random


g_money= 1000
# 创建一个互斥锁
# 默认是未上锁的状态
gCondition = threading.Condition()
gTotalTimes = 10
gTimes = 0

class Producter(threading.Thread):
    def run(self):
        global g_money
        global gTimes
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()  # 上锁
            if gTimes > gTotalTimes:
                gCondition.release()
                break
            g_money += money
            print("%s生产了%d元钱，剩余%d元钱" % (threading.current_thread(),money,g_money))
            gTimes += 1
            gCondition.notify_all()
            gCondition.release()  # 解锁
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global g_money
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()  # 上锁
            while money > g_money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print("余额不足，余额%d,要消费%d" % (g_money,money))

                gCondition.wait()
            g_money -= money
            print("%s消费了%d元钱，剩余%d元钱" % (threading.current_thread(),money,g_money))
            gCondition.release()  # 解锁
            time.sleep(0.5)



def main():
    for i in range(5):
        t1 = Consumer(name="消费者线程%d" % i)
        t1.start()
    for i in range(5):
        t2 = Producter(name="生产者线程%d" % i)
        t2.start()

if __name__ == '__main__':
    main()