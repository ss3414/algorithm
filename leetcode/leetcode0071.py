# ****************************************************************分割线****************************************************************
# todo 0071（Simplify Path）
# 简化路径

class Solution:
    # 池沼算法（TMD，舍不得多给几个使用例）
    def simplifyPath(self, path: str) -> str:
        stack = [i for i in path.split("/")]
        result = ""
        while stack:
            temp = stack.pop()
            if temp != "":
                if temp == ".":
                    if stack:
                        stack.pop()
                elif temp == "..":
                    if stack:
                        stack.pop()
                    if stack:
                        stack.pop()
                else:
                    result = ("/" + temp) + result
        return result if result != "" else "/"

    def simplifyPath2(self, path: str) -> str:
        folders = [i for i in path.split("/") if i != "." and i != ""]
        stack = []
        for i in folders:
            if i == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)

# print(Solution().simplifyPath("/home//foo"))
# print(Solution().simplifyPath("/a//b////c/d//././/.."))
print(Solution().simplifyPath2("/a//b////c/d//././/.."))
