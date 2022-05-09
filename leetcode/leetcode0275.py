# ****************************************************************分割线****************************************************************
# todo 0275（H-Index II）
# H指数II

class Solution:
    # 池沼算法
    def hIndex(self, citations: list) -> int:
        result = []
        left, right = 0, len(citations) - 1
        while left <= right:
            middle = (left + right) // 2
            # print("{l} {r} {m}".format(l=left,r=right,m=middle))
            temp = right - middle + 1
            if citations[middle] <= temp:
                result.append(citations[middle])
                left = middle + 1
            else:
                right = middle
            if left == right:
                break
        return max(result)

    def hIndex2(self, citations: list) -> int:
        l = len(citations)
        left, right = 0, l - 1
        while left <= right:
            middle = (left + right) // 2
            temp = l - middle
            if citations[middle] == temp:
                return temp
            elif citations[middle] > temp:
                right = middle - 1
            else:
                left = middle + 1
        return l - left

# print(Solution().hIndex([0,1,3,5,6]))
# print(Solution().hIndex([0,0,0,0,1,2]))
# print(Solution().hIndex2([100]))
print(Solution().hIndex2([0]))
