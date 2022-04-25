# ****************************************************************分割线****************************************************************
# todo 1352（Product of the Last K Numbers）
# 最后K个数的乘积

# 超时
class ProductOfNumbers:
    def __init__(self):
        self.nums = []
        self.products = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        if len(self.nums) == 1:
            self.products.append(num)
        else:
            self.products = [i * num for i in self.products]
            self.products.append(num)

    def getProduct(self, k: int) -> int:
        return self.products[-k]

class ProductOfNumbers2:
    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)
        print("{n} {p}".format(n=num, p=self.products))

    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0
        return self.products[-1] // self.products[-k - 1]

# obj = ProductOfNumbers()
obj = ProductOfNumbers2()
obj.add(1)
obj.add(2)
obj.add(3)
print(obj.getProduct(1))
print(obj.getProduct(2))
print(obj.getProduct(3))
obj.add(4)
print(obj.getProduct(2))
