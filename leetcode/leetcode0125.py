# ****************************************************************分割线****************************************************************
# todo 0125（Valid Palindrome）
# 验证回文字符串
# 只包括数字和字母，忽略大小写

from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = deque()
        i = 0
        while i < len(s):
            ascii = ord(s[i])
            if (97 <= ascii <= 122) or (48 <= ascii <= 57):
                data.append(chr(ascii))
            elif 97 <= ascii + 32 <= 122:
                data.append(chr(ascii + 32))
            i += 1
        # 双端队列左右同时出，不用考虑奇偶
        while len(data) > 1:
            if data.pop() != data.popleft():
                return False
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
