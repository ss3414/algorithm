# ****************************************************************分割线****************************************************************
# todo 0058（Length of Last Word）
# 最后一个单词的长度

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 字符串全为空格，返回0
        if s.isspace():
            return 0

        # 从左边找最后一个" _"，从右边找第一个"_ "
        length = len(s)
        start = 0
        i = 0
        while i < length - 1:
            if s[i] == " " and s[i + 1] != " ":
                start = i + 1
            i += 1

        end = length
        if length > 0 and s[length - 1] == " ":
            j = length
            while j > start:
                if s[j - 1] == " " and s[j - 2] != " ":
                    end = j - 1
                    break
                j -= 1
        # print("start:{start} end:{end}".format(start=start,end=end))
        # print(s[start:end])
        return len(s[start:end])

    # 抹去右边的空格，再从右往左数到第一个空格即可
    def lengthOfLastWord2(self, s: str) -> int:
        length = 0
        right = len(s) - 1
        while right >= 0 and s[right] == " ":
            right -= 1
        while right >= 0 and s[right] != " ":
            right -= 1
            length += 1
        return length

print(Solution().lengthOfLastWord("Hello"))
print(Solution().lengthOfLastWord("  fly  me  to  the  moon  "))
print(Solution().lengthOfLastWord(" "))
print(Solution().lengthOfLastWord2("Hello"))
print(Solution().lengthOfLastWord2("  fly  me  to  the  moon  "))
print(Solution().lengthOfLastWord2(" "))
