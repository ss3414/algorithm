# ****************************************************************分割线****************************************************************
# todo 0461（Hamming Distance）
# 两个二进制数不同位的个数（汉明距离）

class Solution:
    # 字符串
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        bx, by = bin(x), bin(y)
        bx, by = bx[2::].rjust(32, "0"), by[2::].rjust(32, "0")
        # print("{x} {y}".format(x=bx,y=by))
        i = 0
        while i < len(bx):
            if bx[i] != by[i]:
                count += 1
            i += 1
        return count

    # 位运算（太慢）
    def hammingDistance2(self, x: int, y: int) -> int:
        count = 0
        for i in range(32):
            print("{x} {y}".format(x=x & (1 << i), y=y & (1 << i)))
            if (x & (1 << i)) ^ (y & (1 << i)):
                count += 1
        return count

# print(Solution().hammingDistance(1,4))
print(Solution().hammingDistance2(1, 4))
