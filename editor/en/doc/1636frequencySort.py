from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        fqs = Counter(nums)
        return sorted(nums, key=lambda x: (fqs[x], -x))


assert Solution().frequencySort([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]
