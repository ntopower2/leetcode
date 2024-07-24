from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def mapNumFrom(num) -> int:
            if not mapping:
                return num
            s = str(num)
            s2 = ""
            for c in s:
                s2 += str(mapping[int(c)])
            return int(s2)

        nums.sort(key=mapNumFrom)
        return nums


assert Solution().sortJumbled(
    mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]
) == [338, 38, 991]
