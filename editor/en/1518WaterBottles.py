class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        earned, remained = divmod(numBottles, numExchange - 1)
        res = numBottles + earned
        return res if remained else res - 1


assert Solution().numWaterBottles(9, 3) == 13
