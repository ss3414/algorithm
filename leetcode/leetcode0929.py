# ****************************************************************分割线****************************************************************
# todo 0929（Unique Email Addresses）
# 独特的电子邮件地址

class Solution:
    def numUniqueEmails(self, emails: list) -> int:
        data = set()
        for email in emails:
            temp = ""
            i = 0
            while i < email.index("@"):
                if email[i] == "+":
                    break
                elif email[i] != ".":
                    temp += email[i]
                i += 1
            data.add(temp + "@" + email.split("@")[1])
        return len(data)

print(Solution().numUniqueEmails(["testemail@leetcode.com", "test.email@leetcode.com", "test.e.mail+abc@leetcode.com"]))
