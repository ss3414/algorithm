# ****************************************************************分割线****************************************************************
# todo 1394（Find Lucky Integer in an Array）
# 数组中的幸运数

class Solution:
    def findLucky(self, arr: list) -> int:
        result = -1
        data = {}
        for i in arr:
            if i in data:
                data[i] = data[i] + 1
            else:
                data[i] = 1
        for key, val in data.items():
            if key == val:
                result = max(result, key)
        return result

print(Solution().findLucky([1, 2, 2, 3, 3, 3]))
