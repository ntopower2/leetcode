from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        addedNums = i = 0
        rangeBound = 1
        while rangeBound <= n:
            if i < len(nums) and nums[i] <= rangeBound:
                rangeBound += nums[i]
                i += 1
            else:
                rangeBound *= 2
                addedNums += 1
        return addedNums


assert Solution().minPatches([1, 3], 6) == 1
assert Solution().minPatches([1, 2, 2], 5) == 0
