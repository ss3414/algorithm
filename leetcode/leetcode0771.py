# ****************************************************************分割线****************************************************************
# todo 0771（Jewels and Stones）
# 珠宝与宝石

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum = 0
        for i in jewels:
            sum += stones.count(i)
        return sum

print(Solution().numJewelsInStones("aA", "aAAbbbb"))
