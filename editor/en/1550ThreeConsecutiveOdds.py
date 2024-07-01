from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutiveOdds = 0
        for num in arr:
            if not num % 2:
                consecutiveOdds = 0
            else:
                consecutiveOdds += 1
                if consecutiveOdds == 3:
                    return True
        return False


assert Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]) == True
