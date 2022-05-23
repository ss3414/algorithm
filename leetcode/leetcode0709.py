# ****************************************************************分割线****************************************************************
# todo 0709（To Lower Case）
# 小写字母

class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for i in s:
            if 65 <= ord(i) <= 90:
                result += chr(ord(i) + 32)
            else:
                result += i
        return result

print(Solution().toLowerCase("Hello"))
