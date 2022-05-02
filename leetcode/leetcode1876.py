# ****************************************************************分割线****************************************************************
# todo 1876（Substrings of Size Three with Distinct Characters）
# 字符各不相同的子串

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        i = 0
        while i + 3 <= len(s):
            temp = s[i:i + 3]
            j = 0
            data = {}
            while j < 3:
                if temp[j] in data.keys():
                    break
                data[temp[j]] = 1
                j += 1
                if j == 3:
                    result += 1
            i += 1
        return result

print(Solution().countGoodSubstrings("aababcabc"))
