# ****************************************************************分割线****************************************************************
# todo 0150（Evaluate Reverse Polish Notation）
# 计算逆波兰表达式

class Solution:
    def evalRPN(self, tokens: list) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                right, left = stack.pop(), stack.pop()
                temp = 0
                if i == "+":
                    temp = left + right
                if i == "-":
                    temp = left - right
                if i == "*":
                    temp = left * right
                if i == "/":
                    temp = int(float(left) / right)
                stack.append(temp)
            else:
                stack.append(int(i))
        return int(stack.pop())

# print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
