# ****************************************************************分割线****************************************************************
# todo 0096（Unique Binary Search Trees）
# 不同的二叉搜索树

class Solution:
    # n=0 dp[0]=1 空二叉树也视作BST
    # n=1 dp[1]=1
    # n=2 dp[2]=dp[0]*dp[1]+dp[1]*dp[0]=2
    # n=3 dp[3]=dp[0]*dp[2] 1为根节点，左子树为空，右子树可以有两个数字
    # +dp[1]*dp[1] 2为根节点，左右子树各有一个数字
    # +dp[2]*dp[0] 3为根节点，右子树为空，左子树可以有两个数字
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        i = 2
        while i <= n:
            j = 0
            while j < i:
                dp[i] += dp[j] * dp[i - j - 1]
                j += 1
            i += 1
        print(dp)
        return dp[n]

print(Solution().numTrees(3))
