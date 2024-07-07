class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = emptyBottles = numBottles
        while emptyBottles >= numExchange:
            backFilled, remainedEmpty = divmod(emptyBottles, numExchange)
            drank += backFilled
            emptyBottles = backFilled + remainedEmpty
        return drank


assert Solution().numWaterBottles(9, 3) == 13
