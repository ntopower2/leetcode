from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        arr = SortedList([nums[0]])
        maxL = 1
        headIndex = 0
        for num in nums[1:]:
            arr.add(num)
            while arr and arr[-1] - arr[0] > limit:
                arr.remove(nums[headIndex])
                headIndex += 1
            maxL = max(maxL, len(arr))

        return maxL


assert Solution().longestSubarray([2, 2, 2, 4, 4, 2, 5, 5, 5, 5, 5, 2], 2) == 6
assert Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3
