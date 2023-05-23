# ****************************************************************分割线****************************************************************
# todo 0744（Find Smallest Letter Greater Than Target）
# 寻找大于目标字符的最小字符

class Solution:
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        start, end = letters[0], letters[-1]
        if ord(target) >= ord(end) or ord(target) < ord(start):
            return start
        for i in letters:
            if ord(i) > ord(target):
                return i

print(Solution().nextGreatestLetter(["c", "f", "j"], "a"))
print(Solution().nextGreatestLetter(["c", "f", "j"], "z"))
print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))
