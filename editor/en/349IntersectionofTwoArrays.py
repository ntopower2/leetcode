from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = set(nums1), set(nums2)

        return list(a.intersection(b))


assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
