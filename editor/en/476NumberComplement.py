from math import log2, floor


class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (2 ** floor(log2(num) + 1) - 1) if num else 1


assert Solution().findComplement(5) == 2
