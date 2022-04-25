# ****************************************************************分割线****************************************************************
# todo 0341（Flatten Nested List Iterator）
# 扁平化嵌套列表迭代器

# LeetCode无法AC
class NestedIterator:
    def __init__(self, nestedList: list):
        self.data = self.test(nestedList)
        self.index = 0
        self.length = len(self.data)

    def test(self, input: list) -> list:
        output = []
        for i in input:
            if type(i) == list:
                output += self.test(i)
            else:
                output.append(i)
        return output

    def next(self) -> int:
        if self.index < self.length:
            result = self.data[self.index]
            self.index += 1
            return result
        return 0

    def hasNext(self) -> bool:
        if self.index < self.length:
            return True
        return False

i, v = NestedIterator([1, [2, 3], 4, [5, [6, 7]]]), []
while i.hasNext():
    v.append(i.next())
print(v)
