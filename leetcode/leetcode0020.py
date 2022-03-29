# ****************************************************************分割线****************************************************************
# todo 0020（Valid Parentheses）
# 判断字符串中的括号是否一一对应

from collections import deque

# 利用栈对称的属性，左括号先入栈，碰到右括号如果栈为空或非右括号则字符串无效
def test(s):
    i = 0
    stack = deque()  # 双端队列，同时具有栈和队列的属性
    while i < len(s):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            if (s[i] == ")" and stack.pop() != "(") or (s[i] == "]" and stack.pop() != "[") or (s[i] == "}" and stack.pop() != "{"):
                return False
        i += 1
    # 因为括号一一对应，最后的栈一定是空的
    if len(stack) == 0:
        return True
    else:
        return False

# print(test(")("))
# print(test("([)]"))
print(test("{[]}"))
