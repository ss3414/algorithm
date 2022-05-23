# ****************************************************************分割线****************************************************************
# todo 0946（Validate Stack Sequences）
# 验证出栈顺序

class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        while stack and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
        return len(stack) == 0

print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
