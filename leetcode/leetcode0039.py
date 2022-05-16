# ****************************************************************分割线****************************************************************
# todo 0039（Combination Sum）
# 组合总和

class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        result = []

        def test(current, index, data):
            print("{c} {d}".format(c=current, d=data))
            if current == target:
                result.append(data)
            i = index
            while i < len(candidates):
                if current + candidates[i] > target:
                    return
                # 每次递归将新生成的数组传入
                test(current + candidates[i], i, data + [candidates[i]])
                i += 1
            return

        test(0, 0, [])
        return result

print(Solution().combinationSum([2, 7, 6, 3, 5, 1], 7))
