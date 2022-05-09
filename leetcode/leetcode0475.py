# ****************************************************************分割线****************************************************************
# todo 0475（Heaters）
# 供暖器

class Solution:
    # 太慢
    def findRadius(self, houses: list, heaters: list) -> int:
        def test(heaters, house):
            result = 10 ** 9
            l, r = 0, len(heaters) - 1
            while l <= r:
                mid = (l + r) // 2
                result = min(result, abs(house - heaters[mid]))  # 尽可能计算出离供暖器最近的距离
                if result == 0:  # 房屋和供暖器同坐标
                    return result
                elif heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid - 1
            return result

        radius = 0
        heaters.sort()
        for i in houses:
            radius = max(radius, test(heaters, i))  # 取最大值，因为所有供暖器半径一致
        return radius

print(Solution().findRadius([1, 2, 3, 4, 5, 6], [2, 3, 4]))
