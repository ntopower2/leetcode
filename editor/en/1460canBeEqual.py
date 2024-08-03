from typing import Counter, List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


assert Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]) == False
