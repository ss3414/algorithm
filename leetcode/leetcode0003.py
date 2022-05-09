# ****************************************************************分割线****************************************************************
# todo 0003（Longest Substring Without Repeating Character）
# 无重复字符最长子串

class Solution:
    # 暴力（超时）
    def lengthOfLongestSubstring(self, s: str) -> int:
        def test(s):
            for i in s:
                if s.count(i) > 1:
                    return False
            return True

        i = len(s)
        while i > 0:
            j = 0
            while j + i <= len(s):
                temp = s[j:j + i]
                if test(temp):
                    print(temp)
                    return len(temp)
                j += 1
            i -= 1
        return 0

    # 滑动窗口-边界
    def lengthOfLongestSubstring2(self, s: str) -> int:
        result = 0
        left = -1
        data = {}  # 保存字符和最后出现的位置
        i = 0
        while i < len(s):
            if s[i] in data and data[s[i]] > left:
                left = data[s[i]]
            data[s[i]] = i
            result = max(result, i - left)
            print("{d} {l} {r}".format(d=data, l=left, r=s[left:i]))
            i += 1
        return result

# print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring2("abcabcbb"))
