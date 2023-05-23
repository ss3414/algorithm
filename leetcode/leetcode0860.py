# ****************************************************************分割线****************************************************************
# todo 0860（Lemonade Change）
# 柠檬水找零

class Solution:
    def lemonadeChange(self, bills: list) -> bool:
        data = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                data[5] += 1
            if i == 10:
                data[10] += 1
                if data[5] == 0:
                    return False
                else:
                    data[5] -= 1
            if i == 20:
                if data[10] == 0 and data[5] >= 3:
                    data[5] -= 3
                elif data[10] >= 1 and data[5] >= 1:
                    data[10] -= 1
                    data[5] -= 1
                else:
                    return False
        return True

print(Solution().lemonadeChange([5, 5, 5, 10, 20]))
print(Solution().lemonadeChange([5, 5, 10, 10, 20]))
