from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)

        def findOccurFor(arr: List[int]):
            occur = {}
            for num in arr:
                if not occur.get(num, None):
                    occur[num] = 1
                else:
                    occur[num] += 1
            return occur

        if n < m:
            occur = findOccurFor(nums1)
            other = nums2
        else:
            occur = findOccurFor(nums2)
            other = nums1

        res = []
        for num in other:
            if occur.get(num, None):
                res.append(num)
                occur[num] -= 1

        return res


assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
