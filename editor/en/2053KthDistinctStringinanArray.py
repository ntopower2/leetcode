from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        i = 0
        c = Counter(arr)
        while k and i < len(arr):
            if c[arr[i]] == 1:
                k -= 1
            i += 1

        return "" if k else arr[i - 1]


assert Solution().kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2) == "a"
