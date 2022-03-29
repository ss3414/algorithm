# ****************************************************************分割线****************************************************************
# todo 1534（Count Good Triplets）
# 统计符合条件三元组

class Solution:
    def countGoodTriplets(self, arr: list, a: int, b: int, c: int) -> int:
        count = 0
        i = 0
        while i < len(arr) - 2:
            j = 1
            while j < len(arr) - 1:
                k = 2
                while k < len(arr):
                    if i < j and j < k and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        print("i:{i} j:{j} k:{k}".format(i=i, j=j, k=k))
                        count += 1
                    k += 1
                j += 1
            i += 1
        return count

print(Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
