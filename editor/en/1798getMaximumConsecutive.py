from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        B = 1

        for coin in coins:
            if coin <= B:
                B += coin
            else:
                return B
        return B


assert Solution().getMaximumConsecutive([1, 3]) == 2
