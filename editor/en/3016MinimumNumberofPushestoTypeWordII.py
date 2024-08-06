from collections import Counter
from heapq import heappush, heappop, heapify


class Solution:
    def minimumPushes(self, word: str) -> int:
        available_groups = 8
        res = tmp = 0
        counts = Counter(word)
        heap = [(-val, ltr) for ltr, val in counts.items()]
        heapify(heap)
        while heap:
            val, _ = heappop(heap)
            val *= -1
            res += ((tmp // available_groups) + 1) * val
            tmp += 1

        return res


assert Solution().minimumPushes("aabbccddeeffgghhiiiiii") == 24
