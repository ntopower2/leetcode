#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(set(arr))
        ranks = {}
        for i, num in enumerate(arr2):
            ranks[num] = i + 1
        for i, num in enumerate(arr):
            arr[i] = ranks[num]
        return arr


# @lc code=end

assert Solution().arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]
assert Solution().arrayRankTransform([100, 100, 100]) == [1, 1, 1]
