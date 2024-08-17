from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0]
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        for row in points[1:]:
            left[0] = dp[0]
            right[-1] = dp[-1]
            for i in range(1, n):
                left[i] = max(left[i - 1] - 1, dp[i])
                right[-i - 1] = max(right[-i] - 1, dp[-i - 1])

            dp = [val + max(l, r) for val, l, r in zip(row, left, right)]
        return max(dp)


assert Solution().maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]) == 9
