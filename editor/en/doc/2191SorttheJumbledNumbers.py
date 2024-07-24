from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def mapNumFrom(num) -> int:
            if not mapping:
                return num
            res = i = 0
            d = num
            if d == 0:
                return mapping[0]
            while d > 0:
                d, m = divmod(d, 10)
                res += mapping[m] * (10**i)
                i += 1
            return res

        nums.sort(key=mapNumFrom)
        return nums


assert Solution().sortJumbled(
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert Solution().sortJumbled(
    mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]
) == [338, 38, 991]
