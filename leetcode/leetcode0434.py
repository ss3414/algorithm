# ****************************************************************分割线****************************************************************
# todo 0434（Number of Segments in a String）
# 字符串中的单词数

class Solution:
    # 统计连续非空字符段的数量
    def countSegments(self, s: str) -> int:
        count = 0
        if s == "":
            return count
        s += " "
        i = 0
        while i < len(s) - 1:
            if ord(s[i]) != 32 and ord(s[i + 1]) == 32:
                count += 1
            i += 1
        return count

print(Solution().countSegments(" Hello World "))
