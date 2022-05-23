# ****************************************************************分割线****************************************************************
# todo 0316（Remove Duplicate Letters）
# 删除重复字母，并保持最小字典序

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        data = {}
        for i in range(len(s)):
            data[s[i]] = i  # 记录字符最后出现位置
        print(data)

        stack = []
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                print("{s} {v}".format(s=stack, v=visited))
                while stack and stack[-1] > s[i] and data[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)

print(Solution().removeDuplicateLetters("cbacdcbc"))
