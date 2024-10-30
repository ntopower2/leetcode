#
# @lc app=leetcode id=1671 lang=python3
#
# [1671] Minimum Number of Removals to Make Mountain Array
#

# @lc code=start
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        m = 0

        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                m = i
                break
        if m:
            i = 0
            while i < m and nums[i] < nums[i + 1]:
                i += 1
            while i < n - 1 and nums[i] > nums[i + 1]:
                i += 1
            if i == n - 1:
                return 0

        m = 0
        for i in range(1, n):
            i2 = n - i - 1
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
                j2 = i2 + j + 1
                if nums[i2] > nums[j2]:
                    right[i2] = max(right[i2], right[j2] + 1)

        for l, r in zip(left, right):
            m = max(m, l + r - 1 if l > 1 and r > 1 else 0)

        return n - m


# @lc code=end

assert Solution().minimumMountainRemovals([100, 92, 89, 77, 74, 66, 64, 66, 64]) == 6
assert Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]) == 3
