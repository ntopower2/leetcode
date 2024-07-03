from typing import List
from heapq import nlargest, nsmallest


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        MAX_MOVES = 3
        large = nlargest(MAX_MOVES + 1, nums)
        small = nsmallest(MAX_MOVES + 1, nums)
        # nums.sort()
        # enlarge 3 smallest
        # shorten 3 largest
        # shorten 2 largest, enlarge 1 smallest
        # shorten 1 largest, enlarge 2 smallest
        # nums[-1] - nums[3], large[0] - small[MAX_MOVES+1 - 0]
        # nums[-2] - nums[2], large[1] - small[MAX_MOVES+1 - 1]
        # nums[-3] - nums[1],
        # nums[-4] - nums[0],
        # return min(
        #     [nums[-i] - nums[MAX_MOVES + 1 - i] for i in range(1, MAX_MOVES + 2)]
        # )
        return min([large[i] - small[MAX_MOVES - i] for i in range(MAX_MOVES + 1)])


assert Solution().minDifference([82, 81, 95, 75, 20]) == 1
assert Solution().minDifference([1, 5, 0, 10, 14]) == 1
