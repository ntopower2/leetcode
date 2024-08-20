from functools import lru_cache
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return piles[i]

            return (
                max(piles[i] + dp(i + 1, j), piles[j] - dp(i, j - 1))
                if j - i % 2
                else min(-piles[i] + dp(i + 1, j), -piles[j] - dp(i, j - 1))
            )

        return dp(0, n - 1) > 0 if n % 2 or not sum(piles) % 2 else True


assert Solution().stoneGame([5, 3, 4, 5]) == True
