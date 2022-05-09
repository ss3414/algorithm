# ****************************************************************分割线****************************************************************
# todo 0049（Group Anagrams）
# 异位词分组

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        data = {}
        for letter in strs:
            temp = []
            for i in letter:
                temp.append(i)
            temp = sorted(temp)
            key = " ".join(temp)
            if key in data:
                data[key] += [letter]
            else:
                data[key] = [letter]
        result = []
        for val in data.values():
            result.append(val)
        return result

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
