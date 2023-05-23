# ****************************************************************分割线****************************************************************
# todo 1114（Print in Order）
# 按顺序打印

import threading

def printFirst():
    print("first")

def printSecond():
    print("second")

def printThird():
    print("third")

class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()

    def first(self) -> None:
        printFirst()
        self.event1.set()

    def second(self) -> None:
        if self.event1.wait():
            printSecond()
            self.event2.set()

    def third(self) -> None:
        if self.event2.wait():
            printThird()

obj = Foo()
obj.first()
obj.second()
obj.third()
