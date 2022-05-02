# ****************************************************************分割线****************************************************************
# todo 0914（X of a Kind in a Deck of Cards）
# 卡牌分组

class Solution:
    # 暴力（太慢）
    def hasGroupsSizeX(self, deck: list) -> bool:
        if len(deck) < 2:
            return False

        data = {}
        for i in deck:
            if i in data.keys():
                data[i] = data[i] + 1
            else:
                data[i] = 1
        vals = list(data.values())
        x = 2
        while x <= min(vals):
            j = 0
            while j < len(vals):
                if vals[j] % x != 0:
                    break
                if j == len(vals) - 1:
                    return True
                j += 1
            x += 1
        return False

    # 辗转相除法
    def hasGroupsSizeX2(self, deck: list) -> bool:
        if len(deck) < 2:
            return False

        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)

        data = {}
        for i in deck:
            if i in data.keys():
                data[i] = data[i] + 1
            else:
                data[i] = 1
        vals = list(data.values())
        x = vals[0]
        for val in vals:
            x = gcd(x, val)
        return x > 1

# print(Solution().hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
print(Solution().hasGroupsSizeX2([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
