from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum([e != h for e, h in zip(expected, heights)])


assert Solution().heightChecker([5, 1, 2, 3, 4]) == 5
