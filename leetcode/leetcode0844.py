# ****************************************************************分割线****************************************************************
# todo 0844（Backspace String Compare）
# 比较包含退格的字符串

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for i in s:
            if i == "#" and len(stack1) > 0:
                stack1.pop()
            elif i != "#":
                stack1.append(i)
        for i in t:
            if i == "#" and len(stack2) > 0:
                stack2.pop()
            elif i != "#":
                stack2.append(i)
        print("{s1} {s2}".format(s1=stack1, s2=stack2))
        return stack1 == stack2

# print(Solution().backspaceCompare("ab#c","ad#c"))
# print(Solution().backspaceCompare("a#c","b"))
print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))
