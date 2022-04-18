# ****************************************************************分割线****************************************************************
# todo 0220（Contains Duplicate III）
# 存在重复元素III

class Solution:
    # 滑动窗口（超时）
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        length = len(nums)
        d = 1
        while d <= k:
            left = 0
            right = left + d
            while right < length:
                if abs(nums[left] - nums[right]) <= t:
                    print("{l1} {r1} {l2} {r2}".format(l1=left, r1=right, l2=nums[left], r2=nums[right]))
                    return True
                left += 1
                right += 1
            d += 1
        return False

    # fixme 桶排序
    def containsNearbyAlmostDuplicate2(self, nums: list, k: int, t: int) -> bool:
        buckets = {}
        for i in range(len(nums)):
            bucket_label = nums[i] // (t + 1)
            if bucket_label in buckets:
                return True
            buckets[bucket_label] = nums[i]
            if bucket_label - 1 in buckets and abs(buckets[bucket_label - 1] - nums[i]) <= t:
                return True
            if bucket_label + 1 in buckets and abs(buckets[bucket_label + 1] - nums[i]) <= t:
                return True
            if i >= k:
                del buckets[nums[i - k] // (t + 1)]
        return False

# print(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
print(Solution().containsNearbyAlmostDuplicate2([1, 5, 9, 1, 5, 9], 2, 3))
