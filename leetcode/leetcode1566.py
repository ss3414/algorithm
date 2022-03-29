# ****************************************************************分割线****************************************************************
# todo 1566（Detect Pattern of Length M Repeated K or More Times）
# 长度为M且至少连续重复K次

class Solution:
    def containsPattern(self, arr: list, m: int, k: int) -> bool:
        i = 0
        while i < (len(arr)):
            j = i
            l = k - 1
            while l > 0:
                # print("{temp1} {temp2}".format(temp1=arr[j:j+m],temp2=arr[j+m:j+2*m]))
                if arr[j:j + m] != arr[j + m:j + 2 * m]:
                    break
                j += m
                l -= 1
            if l == 0:
                return True
            i += 1
        return False

# print(Solution().containsPattern([1,2,4,4,4,4],1,3))
# print(Solution().containsPattern([1,2,1,2,1,1,1,3],2,2))
print(Solution().containsPattern([2, 2], 1, 2))
