from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        diffs = [abs(nums[i] - nums[i + 1]) for i in range(n - 1)]
        m, M = min(diffs), nums[-1] - nums[0]

        def pairsWithLeq(diff):
            count = left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > diff:
                    left += 1
                count += right - left
            return count

        while m < M:
            mid = m + (M - m) // 2
            count = pairsWithLeq(mid)

            if count < k:
                m = mid + 1
            else:
                M = mid

        return m


assert Solution().smallestDistancePair([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18) == 2
assert Solution().smallestDistancePair([1, 6, 1], 3) == 5
