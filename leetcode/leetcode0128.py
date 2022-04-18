# ****************************************************************分割线****************************************************************
# todo 0128（Longest Consecutive Sequence）
# 最长连续序列

class Solution:
    # 并查集
    def longestConsecutive(self, nums: list) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)  # 去重
        group, size = {}, {}
        for i in nums:
            group[i] = i  # 1:1,2:2代表每个元素单独构成一个集合
            size[i] = 1

        # 查找
        def find(a):
            if group[a] != a:
                group[a] = find(group[a])
            return group[a]

        # 合并
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:  # 线性压缩，group中每个元素指向根元素，size中根元素挂载多少子元素
                group[rb] = ra
                size[ra] += size[rb]
            # print("--------------------")
            # print("group:{g}".format(g=group))
            # print("size:{s}".format(s=size))

        for i in nums:
            if i - 1 in nums:
                union(i, i - 1)
            if i + 1 in nums:
                union(i, i + 1)
        print("group:{g}".format(g=group))
        print("size:{s}".format(s=size))

        return max(size.values())

print(Solution().longestConsecutive([1, 2, 3, 5, 6, 7, 8]))
