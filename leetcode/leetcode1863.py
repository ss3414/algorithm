# ****************************************************************分割线****************************************************************
# todo 1863（Sum of All Subset XOR Totals）
# 子集异或和的和

class Solution:
    def __init__(self, result=0):
        self.result = result

    # DFS图解
    #                   3,0^5^1^6 3,0^5^1
    #           2,0^5^1
    #     1,0^5
    #           2,0^5
    #                   3,0^5^6 3,0^5
    # 0,0
    #                   3,0^1^6 3,0^1
    #           2,0^1
    #     1,0
    #           2,0
    #                   3,0^6 3,0
    # 排列组合：C(3,0)+C(3,1)+C(3,2)+C(3,3)
    # 排列组合：1+3+3+1
    def subsetXORSum(self, nums: list) -> int:
        def dfs(nums: list, i: int, sum: int):
            print("{i} {s}".format(i=i, s=sum))
            if i == len(nums):
                self.result += sum
                return
            dfs(nums, i + 1, sum ^ nums[i])
            dfs(nums, i + 1, sum)

        if len(nums) == 1:
            return nums[0]
        dfs(nums, 0, 0)
        return self.result

print(Solution().subsetXORSum([5, 1, 6]))
