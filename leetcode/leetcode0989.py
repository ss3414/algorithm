# ****************************************************************分割线****************************************************************
# todo 0989（Add to Array-Form of Integer）
# 数组整数相加

class Solution:
    def addToArrayForm(self, num: list, k: int) -> list:
        temp = int("".join(str(i) for i in num))
        return list(str(temp + k))

print(Solution().addToArrayForm([2, 1, 5], 806))
