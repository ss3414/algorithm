# ****************************************************************分割线****************************************************************
# todo 0150（Evaluate Reverse Polish Notation）
# 计算逆波兰表达式

class Solution:
    def evalRPN(self, tokens: list) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                r, l = stack.pop(), stack.pop()
                t = 0
                if i == "+":
                    t = l + r
                if i == "-":
                    t = l - r
                if i == "*":
                    t = l * r
                if i == "/":
                    t = int(float(l) / r)
                stack.append(t)
            else:
                stack.append(int(i))
        return int(stack.pop())

# print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
