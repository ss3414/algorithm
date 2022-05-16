# ****************************************************************分割线****************************************************************
# todo 0079（Word Search）
# 单词搜索

class Solution:
    def exist(self, board: list, word: str) -> bool:
        def dfs(i, j, index):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True
            else:
                # 临时修改字符而非哈希表避免死循环
                temp = board[i][j]
                board[i][j] = "#"
                result = dfs(i - 1, j, index + 1) or dfs(i + 1, j, index + 1) or dfs(i, j - 1, index + 1) or dfs(i, j + 1, index + 1)
                board[i][j] = temp
                return result

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag = dfs(i, j, 0)
                    if flag:
                        return True
        return False

print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
