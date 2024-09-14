from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = tmp = m = 0

        for num in nums:
            if num > m:
                m = num
                res = tmp = 1
            elif num == m:
                tmp += 1
                res = max(tmp, res)
            else:
                tmp = 0

        return max(res, tmp)


assert (
    Solution().longestSubarray(
        nums=[
            311155,
            311155,
            311155,
            311155,
            311155,
            311155,
            311155,
            311155,
            201191,
            311155,
        ]
    )
    == 8
)
