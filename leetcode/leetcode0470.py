# ****************************************************************分割线****************************************************************
# todo 0470（Implement Rand10() Using Rand7()）
# 用Rand7()实现Rand10()

import random

def rand7():
    return random.randint(1, 7)

class Solution:
    # fixme 拒绝采样
    def rand10(self) -> int:
        while True:
            result = (rand7() - 1) * 7 + rand7()  # 构造rand49()
            if result <= 40:  # 只保留1~40
                return result % 10 + 1

    # fixme 凑概率
    def rand10_2(self) -> int:
        a, b = rand7(), rand7()
        if a > 4 and b < 4:
            return self.rand10()
        else:
            return (a + b) % 10 + 1

print(Solution().rand10())
print(Solution().rand10_2())
