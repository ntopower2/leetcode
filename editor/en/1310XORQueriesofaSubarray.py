from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        for i in range(1, n):
            arr[i] = arr[i - 1] ^ arr[i]

        for i, (l, r) in enumerate(queries):
            queries[i] = arr[r] if not l else arr[r] ^ arr[l - 1]

        return queries


assert Solution().xorQueries(
    arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]
) == [2, 7, 14, 8]
