# ****************************************************************分割线****************************************************************
# todo 0796（Rotate String）
# 旋转字符串

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        goal = list(goal)
        i = 0
        while i < len(s):
            s.append(s.pop(0))
            if s == goal:
                return True
            i += 1
        return False

print(Solution().rotateString("abcde", "cdeab"))
print(Solution().rotateString("abcde", "abced"))
