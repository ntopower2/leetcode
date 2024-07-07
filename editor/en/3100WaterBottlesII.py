from math import sqrt


class Solution:
    def maxBottlesDrunk(self, n: int, d: int) -> int:
        n -= 1
        D = (2 * d - 3) * (2 * d - 3) + 8 * n
        val = 3 - 2 * d + sqrt(D)
        return n + int(val / 2) + 1


assert Solution().maxBottlesDrunk(13, 6) == 15
