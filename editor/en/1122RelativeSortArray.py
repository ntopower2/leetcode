from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        vals = {val: i for i, val in enumerate(arr2)}
        n = len(arr2)

        return sorted(arr1, key=lambda i: vals.get(i, i + n))


assert Solution().relativeSortArray(
    [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
