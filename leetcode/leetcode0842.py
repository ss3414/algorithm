# ****************************************************************分割线****************************************************************
# todo 0842（Split Array into Fibonacci Sequence）
# 将字符串拆分成斐波那契数列

class Solution:
    # 回溯（枚举所有情况，不满足条件跳到下一个分支）
    def splitIntoFibonacci(self, num: str) -> list:
        def backtrack(start, path):
            # 剪枝1（第三项不等于前两项之和）
            if len(path) > 2 and path[-1] != path[-2] + path[-3]:
                return []
            if start >= len(num):
                if len(path) > 2:
                    return path
                return []

            cursor = 0
            result = []
            for i in range(start, len(num)):
                # 剪枝2（数字不能以0开头）
                if i > start and num[start] == "0":
                    return []

                cursor = cursor * 10 + int(num[i])
                # 剪枝3（数字超过最大值）
                if cursor > 2 ** 31 - 1:
                    return []

                path.append(cursor)
                print("{s} {i} {p}".format(s=start, i=i, p=path))
                result = backtrack(i + 1, path)

                # 剪枝4
                if len(result) > 2:
                    return result
                path.pop()
            return result

        return backtrack(0, [])

print(Solution().splitIntoFibonacci("1101111"))
# print(Solution().splitIntoFibonacci("112358130"))
