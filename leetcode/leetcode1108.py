# ****************************************************************分割线****************************************************************
# todo 1108（Defanging an IP Address）
# 无效化IP地址

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

print(Solution().defangIPaddr("1.1.1.1"))
