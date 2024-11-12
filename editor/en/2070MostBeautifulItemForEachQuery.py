#
# @lc app=leetcode id=2070 lang=python3
#
# [2070] Most Beautiful Item for Each Query
#

# @lc code=start
from typing import List
from bisect import bisect_left
from functools import cache


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        maxBeauty = 0
        lastPrice = -1

        @cache
        def getMaxBeauty(query: int) -> int:
            nonlocal maxBeauty, lastPrice
            i = 0

            if query < items[0][0]:
                return 0

            if lastPrice != -1:
                i = bisect_left(items, [lastPrice, 0])

            while i < len(items) and items[i][0] <= query:
                maxBeauty = max(maxBeauty, items[i][1])
                i += 1

            lastPrice = query
            return maxBeauty

        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        answer = [0] * len(queries)

        for idx, query in sorted_queries:
            answer[idx] = getMaxBeauty(query)

        return answer


# @lc code=end

assert Solution().maximumBeauty(
    [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]
) == [2, 4, 5, 5, 6, 6]
