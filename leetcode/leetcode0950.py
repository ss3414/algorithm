# ****************************************************************分割线****************************************************************
# todo 0950（Reveal Cards In Increasing Order）
# 递增顺序显示卡牌

from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        l = len(deck)
        deck = sorted(deck)
        queue = deque([i for i in range(l)])
        result = [None] * l
        j = 0
        while j < l:
            temp = queue.popleft()
            result[temp] = deck[j]
            print("{t} {d}".format(t=temp, d=deck[j]))
            # print("{r} {q}".format(r=result,q=queue))
            if queue:
                next = queue.popleft()
                queue.append(next)
            j += 1
        return result

print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
