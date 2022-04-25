# ****************************************************************分割线****************************************************************
# todo 0933（Number of Recent Calls）
# 最近的请求次数

from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque([])

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while t - 3000 > self.queue[0]:
            self.queue.popleft()
        return len(self.queue)

obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
