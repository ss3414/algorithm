# ****************************************************************分割线****************************************************************
# todo 0040（Combination Sum II）
# 组合总和II

class Solution:
    # 超时
    def combinationSum2(self, candidates: list, target: int) -> list:
        def test(current, index, data):
            print("index:{i} current:{c} {d}".format(i=index, c=current, d=data))
            if current == target and data not in result:
                result.append(data)
            i = index
            while i < len(candidates):
                if current + candidates[i] > target:
                    return
                # 每次递归将新数组、新坐标传入
                test(current + candidates[i], i + 1, data + [candidates[i]])
                i += 1
            return

        candidates.sort()
        result = []
        test(0, 0, [])
        return result

    def combinationSum3(self, candidates: list, target: int) -> list:
        def test(target, index, data):
            if target == 0:
                return [data[:]]
            if target < 0:
                return []

            result = []
            while index < len(candidates):
                data.append(candidates[index])
                result.extend(test(target - candidates[index], index + 1, data))
                data.pop()
                cursor = candidates[index]
                index += 1
                while index < len(candidates):
                    if cursor != candidates[index]:
                        break
                    index += 1
            return result

        candidates.sort()
        return test(target, 0, [])

# print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
print(Solution().combinationSum3([10, 1, 2, 7, 6, 1, 5], 8))
