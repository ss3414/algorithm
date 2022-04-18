# ****************************************************************分割线****************************************************************
# todo 0605（Can Place Flowers）
# 种花

class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        if len(flowerbed) == 0:
            return False
        # 如果左右边界是0，扩张边界
        if flowerbed[0] == 0:
            flowerbed.insert(0, 0)
        if flowerbed[-1] == 0:
            flowerbed.append(0)
        print(flowerbed)
        sum = 0
        count = 0
        i = 0
        while i <= len(flowerbed):
            if i < len(flowerbed) and flowerbed[i] == 0:
                count += 1
            else:
                if count > 0:
                    sum += (count - 1) // 2  # 连续count个0，则可以放(count-1)/2盆花
                count = 0
            print("{c} {s}".format(c=count, s=sum))
            i += 1
        return sum >= n

# print(Solution().canPlaceFlowers([0, 1, 0, 0, 0, 1, 0], 2))
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
