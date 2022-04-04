# ****************************************************************分割线****************************************************************
# todo 0482（License Key Formatting）
# 密钥格式化
# 第一组可以比k短

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = ""
        temp = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] != "-" and len(temp) < k:
                temp = s[i] + temp
            if len(temp) == k or i == 0:
                result = "-" + temp + result
                temp = ""
            i -= 1
        return result.lstrip("-").upper()

    # 去掉间隔符逆序，每隔k个添加间隔符再逆序
    def licenseKeyFormatting2(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]
        return "-".join(s[i:i + k] for i in range(0, len(s), k))[::-1]

# print(Solution().licenseKeyFormatting("2-5g-3-j",4))
# print(Solution().licenseKeyFormatting("--a-a-a-a--",2))

print(Solution().licenseKeyFormatting2("--a-a-a-a--", 2))
