# ****************************************************************分割线****************************************************************
# todo 1588（Sum of All Odd Length Subarrays）
# 奇数长度子数组的和

class Solution:
    # fixme 前缀和
    def sumOddLengthSubarrays(self, arr: list) -> int:
        l = len(arr)
        prefix = [0] * (l + 1)
        i = 0
        while i < l:
            prefix[i + 1] = prefix[i] + arr[i]
            i += 1
        result = 0
        i = 0
        while i < l:
            j = i
            while j >= 0:
                result += (prefix[i + 1] - prefix[j])
                j -= 2
            i += 1
        return result

print(Solution().sumOddLengthSubarrays([1, 2, 3, 4, 5]))
