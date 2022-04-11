# ****************************************************************分割线****************************************************************
# todo 1201（Ugly Number III）
# 丑数III

class Solution:
    # 暴力（超时）
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        result = []
        i, j, k = 1, 1, 1
        while len(result) < n:
            t1 = a * i
            t2 = b * j
            t3 = c * k
            temp = min(t1, t2, t3)
            if temp == t1:
                i += 1
            if temp == t2:
                j += 1
            if temp == t3:
                k += 1
            result.append(temp)
        print(result)
        return result[-1]

    # 在1~n的范围内，丑数=a的倍数（n/a）+b的倍数（n/b）+c的倍数（n/c）-ab的公倍数-ac的
    # 公倍数-bc的公倍数+abc的公倍数
    def nthUglyNumber2(self, n: int, a: int, b: int, c: int) -> int:
        # 最大公约数
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)

        # 最小公倍数
        def lcm(a, b):
            return a * b / gcd(a, b)

        # 二分法
        left, right = 0, 2e9
        while left < right:
            middle = left + (right - left) // 2
            temp = middle // a + middle // b + middle // c - middle // lcm(a, b) - middle // lcm(a, c) - middle // lcm(b, c) + middle // lcm(a, lcm(b, c))
            print("{l} {m} {r} {t}".format(l=left, m=middle, r=right, t=temp))
            if temp < n:
                left = middle + 1
            else:
                right = middle
        return int(right)

# print(Solution().nthUglyNumber(22,2,3,5))
print(Solution().nthUglyNumber2(3, 2, 3, 5))
