# ****************************************************************分割线****************************************************************
# todo 1047（Remove All Adjacent Duplicates In String）
# 删除相邻重复项

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

print(Solution().removeDuplicates("abbaca"))
