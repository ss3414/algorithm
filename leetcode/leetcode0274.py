# ****************************************************************分割线****************************************************************
# todo 0274（H-Index）
# H指数

class Solution:
    def hIndex(self, citations: list) -> int:
        citations.sort()
        l = h = len(citations)
        for i in citations:
            if i >= h:
                return h
            h -= 1
        return 0

# print(Solution().hIndex([1,3,1]))
print(Solution().hIndex([1, 2, 3, 4, 5]))
