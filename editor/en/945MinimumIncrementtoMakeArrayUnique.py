from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        last = -1
        res = 0
        for i in range(len(nums)):
            if last == nums[i]:
                res += 1
                nums[i] += 1
            elif last > nums[i]:
                res += last + 1 - nums[i]
                nums[i] = last + 1
            last = nums[i]
        return res


assert Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]) == 6
