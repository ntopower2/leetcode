#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = i = tmp = 0
        arrNums = Counter(nums[:k])
        tmp = sum(nums[:k])
        if len(arrNums) == k:
            res = tmp

        i = k
        while i < len(nums):
            arrNums[nums[i - k]] -= 1
            if not arrNums[nums[i - k]]:
                del arrNums[nums[i - k]]
            arrNums[nums[i]] += 1
            tmp -= nums[i - k]
            tmp += nums[i]
            if len(arrNums) == k:
                res = max(tmp, res)

            i += 1

        return res


# @lc code=end

assert Solution().maximumSubarraySum([1, 1, 1, 7, 8, 9], k=3) == 24
