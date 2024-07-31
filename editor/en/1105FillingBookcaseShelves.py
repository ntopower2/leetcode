from functools import lru_cache
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        @lru_cache(None)
        def dp(i, currentHeight=0, widthLeft=shelfWidth):
            if i == len(books):
                return currentHeight
            bw, bh = books[i]
            res = dp(i + 1, bh, shelfWidth - bw) + currentHeight

            if bw <= widthLeft:
                res = min(res, dp(i + 1, max(currentHeight, bh), widthLeft - bw))

            return res

        return dp(0)


assert (
    Solution().minHeightShelves(
        books=[[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], shelfWidth=4
    )
    == 6
)
