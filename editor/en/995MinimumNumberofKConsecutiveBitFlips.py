from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        if k == 1:
            return len(nums) - sum(nums)

        flips = 0
        n = len(nums)
        isCurFlipped = False
        isFlippedAt = [False] * n

        for i, num in enumerate(nums):
            if i >= k:
                isCurFlipped ^= isFlippedAt[i - k]
            if num == isCurFlipped:
                if i + k > n:
                    return -1
                isCurFlipped ^= True
                isFlippedAt[i] = True
                flips += 1

        return flips


assert Solution().minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3) == 3
