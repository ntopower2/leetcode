from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        res = []
        if m * n != l:
            return []

        for i in range(m):
            res.append(original[i * n : (i + 1) * n])

        return res


assert Solution().construct2DArray(original=[1, 2, 3, 4], m=2, n=2) == [[1, 2], [3, 4]]
