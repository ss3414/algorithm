# ****************************************************************分割线****************************************************************
# todo 0125（Valid Palindrome）
# 是否为回文串
# 只包括数字/字母，忽略大小写

from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        data = deque()
        i = 0
        while i < len(s):
            ascii = ord(s[i])
            if (ascii >= 97 and ascii <= 122) or (ascii >= 48 and ascii <= 57):
                data.append(chr(ascii))
            elif ascii + 32 >= 97 and ascii + 32 <= 122:
                data.append(chr(ascii + 32))
            i += 1
        # 双端队列左右同时出，不用考虑奇偶
        while len(data) > 1:
            if data.pop() != data.popleft():
                return False
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
