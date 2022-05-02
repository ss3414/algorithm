# ****************************************************************分割线****************************************************************
# todo 0227（Basic Calculator II）
# 计算器II

class Solution:
    # 池沼算法（TMD，多给几个使用例会死）
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack1 = []
        i = 0
        digit = ""
        while i < len(s):
            if s[i] not in "+-*/":
                digit += s[i]
            else:
                stack1.append(digit)
                digit = ""
                temp = s[i]
                if s[i] == "*":
                    left, right = int(stack1.pop()), int(s[i + 1])
                    temp = left * right
                    i += 1
                elif s[i] == "/":
                    left, right = int(stack1.pop()), int(s[i + 1])
                    temp = left // right
                    i += 1
                stack1.append(temp)
            i += 1

        stack2 = []
        j = 0
        while j < len(stack1):
            temp = stack1[j]
            if stack1[j] == "+":
                left, right = int(stack2.pop()), int(stack1[j + 1])
                temp = left + right
                j += 1
            elif stack1[j] == "-":
                left, right = int(stack2.pop()), int(stack1[j + 1])
                temp = left - right
                j += 1
            stack2.append(temp)
            j += 1
        result = ""
        for k in stack2:
            result += str(k)
        return int(result)

    def calculate2(self, s: str) -> int:
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    temp = stack.pop()
                    if temp // num < 0 and temp % num != 0:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                sign = s[i]
                num = 0
        return sum(stack)

# print(Solution().calculate("42"))
# print(Solution().calculate("3+5 / 2"))
# print(Solution().calculate("12-3*4"))
print(Solution().calculate2("0"))
