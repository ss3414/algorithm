# ****************************************************************分割线****************************************************************
# todo 0388（Longest Absolute File Path）
# 最长绝对文件路径

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        level = 0
        letters = 0
        flag = False
        result = 0
        for s in input:
            if s == "\n":
                if flag:
                    result = max(result, sum(stack) + letters)
                else:
                    stack.append(letters + 1)
                letters = 0
                flag = False
            elif s == "\t":
                level += 1
            else:
                if not letters:
                    stack = stack[:level]
                    level = 0
                letters += 1
                flag |= (s == ".")
        if flag:
            result = max(result, sum(stack) + letters)
        return result

print(Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
