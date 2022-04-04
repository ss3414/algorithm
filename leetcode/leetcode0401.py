# ****************************************************************分割线****************************************************************
# todo 0401（Binary Watch）
# 二进制手表

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list:
        result = []
        # 遍历24小时，把对应时间转成二进制字符串，再统计1的个数
        for h in range(12):
            for m in range(60):
                temp = bin(h) + bin(m)
                if temp.count("1") == turnedOn:
                    time = "%d:%02d" % (h, m)
                    result.append(time)
        return result

print(Solution().readBinaryWatch(1))
