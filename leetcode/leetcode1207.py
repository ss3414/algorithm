# ****************************************************************分割线****************************************************************
# todo 1207（Unique Number of Occurrences）
# 独一无二的出现次数

class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        data = {}
        for i in arr:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        return len(data.values()) == len(set(data.values()))

print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(Solution().uniqueOccurrences([1, 2]))
