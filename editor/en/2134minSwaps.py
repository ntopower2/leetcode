from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numOnes = nums.count(1)
        if numOnes == len(nums):
            return 0

        res = numZeroes = nums[:numOnes].count(0)
        for i in range(numOnes, len(nums) + numOnes):
            if nums[i % len(nums)] != nums[i - numOnes]:
                numZeroes += 1 if nums[i - numOnes] else -1

            res = min(res, numZeroes)
        return res


assert Solution().minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]) == 2
