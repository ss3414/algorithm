# ****************************************************************分割线****************************************************************
# todo 0187（Repeated DNA Sequences）
# 重复的DNA序列

class Solution:
    # 滑动窗口
    def findRepeatedDnaSequences(self, s: str) -> list:
        result = []
        data = {}
        i = 0
        while i + 10 <= len(s):
            temp = s[i:i + 10]
            if temp in data.keys():
                data.update({temp: data[temp] + 1})
            else:
                data.update({temp: 1})
            i += 1
        for key, val in data.items():
            if val > 1:
                result.append(key)
        return result

print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
