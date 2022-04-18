# ****************************************************************分割线****************************************************************
# todo 1790（Check if One String Swap Can Make Strings Equal）
# 字符交换

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        def test(s):
            data = {}
            for i in s:
                if i in data:
                    data[i] += 1
                else:
                    data[i] = 1
            return data

        data1, data2 = test(s1), test(s2)
        for key in data1.keys():
            if (key not in data2) or data1[key] != data2[key]:
                return False

        count = 0
        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                count += 1
            i += 1
        return count <= 2

# print(Solution().areAlmostEqual("bank","kanb"))
print(Solution().areAlmostEqual("attack", "defend"))
