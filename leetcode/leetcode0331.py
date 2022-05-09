# ****************************************************************分割线****************************************************************
# todo 0331（Verify Preorder Serialization of a Binary Tree）
# 根据前序遍历序列化验证二叉树

class Solution:
    # 序列化
    # 左长腿：1,2,3,#,#,#,#（不能有超过3个#存在？）
    # 右长腿：1,#,2,#,3,#,#
    # 满二叉树：1,2,#,#,3,#,#
    # 奇数个字符，#总比数字多一个
    def isValidSerialization(self, preorder: str) -> bool:
        data = preorder.split(",")
        print(data)
        count = 0
        i = 0
        while i < len(data) - 1:
            if data[i] == "#":
                if count == 0:
                    return False
                count -= 1
            else:
                count += 1
            i += 1
        return count == 0 and data[-1] == "#"

print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
