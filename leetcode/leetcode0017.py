# ****************************************************************分割线****************************************************************
# todo 0017（Letter Combinations of a Phone Number）
# 电话号码的字母组合

class Solution:
    def letterCombinations(self, digits: str) -> list:
        if digits == "":
            return []

        result = [""]
        data = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        i = 0
        while i < len(digits):
            temp = []
            letter = data[int(digits[i])]
            j = 0
            while j < len(letter):
                for s in result:
                    temp.append(s + letter[j])
                j += 1
            print(temp)
            result = temp
            i += 1
        return result

print(Solution().letterCombinations("23"))
# print(Solution().letterCombinations(""))
