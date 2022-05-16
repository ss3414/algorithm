# ****************************************************************分割线****************************************************************
# todo 0395（Longest Substring with At Least K Repeating Characters）
# 至少有K个重复字符的最长子串
# 子串中的每个字符频率都要大于K

class Solution:
    # 池沼算法
    def longestSubstring(self, s: str, k: int) -> int:
        data = {}
        for i in s:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        for key, val in data.items():
            if val < k:
                s = s.replace(key, "#")

        if "#" not in s:
            return len(s)
        else:
            result = 0
            for i in s.split("#"):
                if len(i) >= k:
                    j = 0
                    while j < len(i):
                        if i.count(i[j]) < k:
                            break
                        j += 1
                        if j == len(i):
                            result = max(result, len(i))
            return result

    # 二分法
    def longestSubstring2(self, s: str, k: int) -> int:
        def test(s, start, end):
            if end - start < k:
                return 0

            data = {}
            i = start
            while i < end:
                if s[i] in data:
                    data[s[i]] += 1
                else:
                    data[s[i]] = 1
                i += 1
            i = start
            while i < end:
                if data[s[i]] < k:
                    j = i + 1
                    while j < end and data[s[j]] < k:
                        j += 1
                    return max(test(s, start, i), test(s, j, end))
                i += 1
            return end - start

        return test(s, 0, len(s))

# print(Solution().longestSubstring("bbaaacbd", 2))
print(Solution().longestSubstring2("bbaaacbd", 2))
