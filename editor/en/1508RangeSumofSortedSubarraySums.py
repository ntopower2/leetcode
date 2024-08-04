from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sortedSums = [0 for _ in range(n * (n + 1) // 2)]
        i = k = 0
        while i < n:
            tmp = 0
            for j in range(i, n):
                tmp += nums[j]
                sortedSums[k] = tmp
                k += 1
            i += 1
        sortedSums.sort()
        return sum(sortedSums[left - 1 : right]) % (10**9 + 7)


assert Solution().rangeSum([100] * 1000, 1000, 1, 500500) == 716699888
assert Solution().rangeSum(list(range(1, 5)), 4, 3, 4) == 6
