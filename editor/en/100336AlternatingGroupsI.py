from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        groups = 0

        for i in range(n):
            if (
                colors[i] != colors[(i + 1) % n]
                and colors[i] != colors[(i - 1 + n) % n]
            ):
                groups += 1

        return groups


assert Solution().numberOfAlternatingGroups([0, 1, 0, 1]) == 4
assert Solution().numberOfAlternatingGroups([1, 1, 1]) == 0
