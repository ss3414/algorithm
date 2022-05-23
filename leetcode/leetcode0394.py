# ****************************************************************分割线****************************************************************
# todo 0394（Decode String）
# 解码字符串

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "]":
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                digit = ""
                while stack and len(stack[-1]) == 1 and 57 >= ord(stack[-1]) >= 48:
                    digit = stack.pop() + digit
                # print("{d} {t}".format(d=digit,t=temp))
                temp *= int(digit)
                stack.append(temp)
            else:
                stack.append(i)
        return "".join(stack)

print(Solution().decodeString("3[a2[c]]"))
# print(Solution().decodeString("3[a]2[bc]"))
