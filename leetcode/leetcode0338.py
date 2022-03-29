# ****************************************************************分割线****************************************************************
# todo 0338（Counting Bits）
# 比特位计数

class Solution:
    # 暴力
    def countBits(self, n: int) -> list:
        result = []
        i = 0
        while i <= n:
            count = 0
            j = i
            while j > 0:
                count += (j & 1)
                j >>= 1
            result.append(count)
            i += 1
        return result

    # fixme 规律（DP）
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # 0 1 1 2 1 2 2 3 1 2 2  3  2  3  3  4
    def countBits2(self, n: int) -> list:
        if n == 0:
            return [0]
        result = [0, 1]
        i, k = 2, 2
        while i <= n:
            i = pow(2, k - 1)
            while i < pow(2, k):
                if i > n:
                    break
                temp = (pow(2, k) - pow(2, k - 1)) // 2
                if i < pow(2, k - 1) + temp:
                    result.append(result[i - temp])
                else:
                    result.append(result[i - temp] + 1)
                i += 1
            k += 1
        return result

# print(Solution().countBits(5))
print(Solution().countBits2(5))
