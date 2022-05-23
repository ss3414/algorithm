# ****************************************************************分割线****************************************************************
# todo 0636（Exclusive Time of Functions）
# 函数执行时间

class Solution:
    def exclusiveTime(self, n: int, logs: list) -> list:
        result = [0] * n
        current = []
        for log in logs:
            fun, code, time = log.split(":")
            fun, time = int(fun), int(time)
            print(current)
            if code == "start":
                if current:
                    id, started = current[-1]
                    result[id] += (time - started)
                current.append([fun, time])
            else:
                id, started = current.pop()
                result[id] += (time - started + 1)
                if current:
                    current[-1][1] = time + 1
        return result

print(Solution().exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
