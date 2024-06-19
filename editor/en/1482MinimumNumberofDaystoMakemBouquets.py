from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        totalNeeded = m * k
        if totalNeeded > n:
            return -1
        if totalNeeded == n:
            return max(bloomDay)

        def canMake(days: int) -> bool:
            tmpK = 0
            tmpM = m
            for bloom in bloomDay:
                if bloom <= days:
                    tmpK += 1
                    if tmpK == k:
                        tmpK = 0
                        tmpM -= 1
                else:
                    tmpK = 0
                if not tmpM:
                    return True

            return False

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if canMake(mid):
                r = mid
            else:
                l = mid + 1
        return l


assert Solution().minDays([1, 10, 3, 10, 2], 3, 1) == 3
assert Solution().minDays([7, 7, 7, 7, 12, 7, 7], 2, 3) == 12
