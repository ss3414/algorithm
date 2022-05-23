# ****************************************************************分割线****************************************************************
# todo 0682（Baseball Game）
# 棒球游戏

class Solution:
    def calPoints(self, ops: list) -> int:
        stack = []
        for i in ops:
            if i not in ["C", "D", "+"]:
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
        return sum(stack)

print(Solution().calPoints(["5", "2", "C", "D", "+"]))
