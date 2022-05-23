# ****************************************************************分割线****************************************************************
# todo 0657（Robot Return to Origin）
# 机器人是否能返回原点

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        data = {"L": 0, "R": 0, "U": 0, "D": 0}
        for i in moves:
            if i in data:
                data[i] += 1
        return data["L"] == data["R"] and data["U"] == data["D"]

print(Solution().judgeCircle("UD"))
print(Solution().judgeCircle("LL"))
