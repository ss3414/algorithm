# ****************************************************************分割线****************************************************************
# todo 0242（Valid Anagram）
# 字母异位词
# 两字符串字母出现次数相同

class Solution:
    # 哈希表
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        data = {}
        i = 0
        while i < len(s):
            s1 = data.get(s[i])
            if s1 is None:
                data[s[i]] = 1
            else:
                data[s[i]] = s1 + 1
            t1 = data.get(t[i])
            if t1 is None:
                data[t[i]] = -1
            else:
                data[t[i]] = t1 - 1
            i += 1
        # s用正数，t用负数，如果字母出现次数相同，则最终只剩0
        if max(data.values()) > 0 or min(data.values()) < 0:
            return False
        else:
            return True

    # 简化版
    def isAnagram2(self, s: str, t: str) -> bool:
        data1, data2 = {}, {}
        for i in s:
            data1[i] = data1.get(i, 0) + 1
        for i in t:
            data2[i] = data2.get(i, 0) + 1
        return data1 == data2

print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
print(Solution().isAnagram2("anagram", "nagaram"))
print(Solution().isAnagram2("rat", "car"))
