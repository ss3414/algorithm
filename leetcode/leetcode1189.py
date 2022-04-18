# ****************************************************************分割线****************************************************************
# todo 1189（Maximum Number of Balloons）
# 凑气球（木桶原理）

class Solution:
    # 池沼算法
    def maxNumberOfBalloons(self, text: str) -> int:
        data = {}
        for i in text:
            if i in data.keys():
                data.update({i: data[i] + 1})
            else:
                data.update({i: 1})
        for key, val in data.items():
            if key in ["a", "b", "n"]:
                data[key] -= 1
            if key in ["l", "o"]:
                data[key] -= 2
        return 0

    def maxNumberOfBalloons2(self, text: str) -> int:
        data = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in data:
                data[char] += 1
        data["l"] //= 2
        data["o"] //= 2
        return min(data.values())

# print(Solution().maxNumberOfBalloons("balllllllllllloooooooooon"))
print(Solution().maxNumberOfBalloons2("balllllllllllloooooooooon"))
