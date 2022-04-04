# ****************************************************************分割线****************************************************************
# todo 0383（Ransom Note）
# 赎金信

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        data = {}
        for i in magazine:
            if i in data.keys():
                data.update({i: data[i] + 1})
            else:
                data.update({i: 1})
        count = 0
        for j in ransomNote:
            if j in data.keys() and data[j] > 0:
                data.update({j: data[j] - 1})
                count += 1
        return count == len(ransomNote)

print(Solution().canConstruct("a", "ab"))
