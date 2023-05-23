# ****************************************************************分割线****************************************************************
# todo 0944（Delete Columns to Make Sorted）
# 删列造序

class Solution:
    def minDeletionSize(self, strs: list) -> int:
        l = len(strs[0])
        grids = [None] * l
        for word in strs:
            i = 0
            while i < l:
                if grids[i] is None:
                    grids[i] = []
                grids[i].append(word[i])
                i += 1
        count = 0
        for j in grids:
            if j != sorted(j):
                count += 1
        return count

print(Solution().minDeletionSize(["abcd", "bcda"]))
