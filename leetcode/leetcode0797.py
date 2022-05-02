# ****************************************************************分割线****************************************************************
# todo 0797（All Paths From Source to Target）
# 所有可能的路径

class Solution:
    # 池沼算法
    def allPathsSourceTarget(self, graph: list) -> list:
        result = []
        n = len(graph)

        def dfs(index: int, path: list):
            # print("{i} {p}".format(i=index,p=path))
            if graph[index] == []:
                result.append(path + [n - 1])
            for i in graph[index]:
                dfs(i, path + [index])

        for i in graph[0]:
            dfs(i, [0])
        return result

    def allPathsSourceTarget2(self, graph: list) -> list:
        result = []
        n = len(graph)

        def dfs(index: int, path: list):
            if index == n - 1:
                result.append(path)
            else:
                for i in graph[index]:
                    dfs(i, path + [i])

        dfs(0, [0])
        return result

# print(Solution().allPathsSourceTarget([[2],[],[1]]))
print(Solution().allPathsSourceTarget2([[4, 3, 1], [3, 2, 4], [3], [4], []]))
