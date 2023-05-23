# ****************************************************************分割线****************************************************************
# todo 0925（Long Pressed Name）
# 长按键入

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        a, b = len(name), len(typed)
        while i < a and j < b:
            if name[i] == typed[j]:
                i += 1
                j += 1
                continue
            elif i != 0 and name[i - 1] == typed[j]:
                j += 1
            else:
                return False
        if i < a:
            return False
        if j < b:
            while j < b:
                if name[a - 1] != typed[j]:  # name末尾字符要与typed剩余字符一致
                    return False
                j += 1
        return True

# print(Solution().isLongPressedName("alex","aaleex"))
# print(Solution().isLongPressedName("saeed","ssaaedd"))
print(Solution().isLongPressedName("vtkgn", "vttkgnn"))
