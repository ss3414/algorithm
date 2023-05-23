# ****************************************************************分割线****************************************************************
# todo 0941（Valid Mountain Array）
# 山脉数组

class Solution:
    def validMountainArray(self, arr: list) -> bool:
        max_val = max(arr)
        index = arr.index(max_val)
        left, right = arr[0:index + 1], arr[index::]
        print("{l} {r}".format(l=left, r=right))
        if len(left) <= 1 or len(right) <= 1:
            return False
        i = 0
        while i < len(left) - 1:
            if left[i + 1] <= left[i]:
                return False
            i += 1
        j = 0
        while j < len(right) - 1:
            if right[j + 1] >= right[j]:
                return False
            j += 1
        return True

print(Solution().validMountainArray([2, 3, 1]))
# print(Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9]))
