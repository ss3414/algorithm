# ****************************************************************分割线****************************************************************
# todo 0212（Word Search II）
# 单词搜索II

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        cursor = self
        for i in word:
            if i not in cursor.children:
                cursor.children[i] = TrieNode()
            cursor = cursor.children[i]
        cursor.is_word = True

class Solution:
    # DFS（超时）
    def findWords(self, board: list, words: list) -> list:
        def dfs(i, j, word, index, data, string):
            # print(string)
            # print(data)
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index] or (i, j) in data:
                return False

            # 这里使用哈希表可能会导致污染，每次传递新生成的数组又会导致超时
            # data[(i,j)]=board[i][j]
            data.append((i, j))
            string += board[i][j]
            if index == len(word) - 1:  # 到达单词结尾
                return True
            else:
                return dfs(i - 1, j, word, index + 1, data + [], string) or dfs(i + 1, j, word, index + 1, data + [], string) or dfs(i, j - 1, word, index + 1, data + [], string) or dfs(i, j + 1, word, index + 1, data + [], string)

        m, n = len(board), len(board[0])
        intital = [word[0] for word in words]  # 单词首字母对应坐标
        coordinate = []
        i = 0
        while i < m:
            j = 0
            while j < n:
                if board[i][j] in intital:
                    coordinate.append((i, j))
                j += 1
            i += 1
        # print(coordinate)

        result = []
        for word in words:
            for i, j in coordinate:
                if board[i][j] == word[0]:
                    flag = dfs(i, j, word, 0, [], "")
                    if flag:
                        result.append(word)
                        break
        return result

    # 字典树+DFS（太慢）
    def findWords2(self, board: list, words: list) -> list:
        def dfs(i, j, root, word):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in root.children or (i, j) in data:
                return

            data.add((i, j))
            root = root.children[board[i][j]]
            word += board[i][j]
            if root.is_word:
                result.add(word)
            dfs(i - 1, j, root, word)
            dfs(i + 1, j, root, word)
            dfs(i, j - 1, root, word)
            dfs(i, j + 1, root, word)
            data.remove((i, j))

        root = TrieNode()
        for word in words:
            root.insert(word)

        m, n = len(board), len(board[0])
        result, data = set(), set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i, j, root, "")
        return result

# print(Solution().findWords(
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# ["oath","pea","eat","rain"]))

print(Solution().findWords2(
    [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
    ["oath", "pea", "eat", "rain"]))
