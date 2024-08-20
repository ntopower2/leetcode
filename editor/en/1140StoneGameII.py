from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dpValues = {}
        n = len(piles)
        suffixSumFrom = [piles[n - 1]] * n

        for i in range(n - 2, -1, -1):
            suffixSumFrom[i] = suffixSumFrom[i + 1] + piles[i]

        def dp(i: int, m: int) -> int:
            if i >= n:
                return 0
            if (i, m) in dpValues:
                return dpValues[(i, m)]

            val = 0
            for x in range(1, 2 * m + 1):
                if i + x <= n:
                    val = max(val, suffixSumFrom[i] - dp(i + x, max(x, m)))

            dpValues[(i, m)] = val
            return val

        return dp(0, 1)


assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10
