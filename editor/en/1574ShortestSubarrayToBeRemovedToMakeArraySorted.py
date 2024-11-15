#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#

# @lc code=start
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        left, right = 0, n - 1
        while left < n - 1 and arr[left + 1] >= arr[left]:
            left += 1

        if left == n - 1:
            return 0

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        res = min(n - left - 1, right)
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        return res


# @lc code=end

assert Solution().findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1]) == 3
