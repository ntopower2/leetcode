from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        remainder = k % sum(chalk)
        while remainder and remainder >= chalk[i]:
            remainder -= chalk[i]
            i += 1

        return i


assert Solution().chalkReplacer([3, 4, 1, 2], 25) == 1
assert Solution().chalkReplacer([5, 1, 5], 22) == 0
