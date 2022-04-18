# ****************************************************************分割线****************************************************************
# todo 0053（Maximum Subarray）
# 最大子数组的和
# 子数组必须连续

# 暴力（超时）
def test(nums: list):
    max = -10000
    length = 1  # 子数组的长度
    while length <= len(nums):
        i = 0
        while i <= len(nums) - length:
            # print("sub:{sub} sum:{sum}".format(sub=nums[i:i+length],sum=sum(nums[i:i+length])))
            if sum(nums[i:i + length]) > max:
                max = sum(nums[i:i + length])
            i += 1
        length += 1
    return max

# fixme Kadane's Algorithm（卡达内算法）
def test2(nums: list):
    result = -10000
    sum = 0
    for num in nums:
        print("sum:{sum} num:{num} result:{result}".format(sum=sum, num=num, result=result))
        sum = max(sum + num, num)  # sum不断累加触碰最大值，一旦sum大于result，则为新的最大和数组
        result = max(result, sum)
    return result

# print(test([-2,1,-3,4,-1,2,1,-5,4]))
# print(test([1]))

# print(test2([2,-1,-1,1]))
print(test2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
