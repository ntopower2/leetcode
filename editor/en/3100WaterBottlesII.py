class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = emptyBottles = numBottles
        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            numExchange += 1
            drank += 1
            emptyBottles += 1
        return drank


assert Solution().maxBottlesDrunk(13, 6) == 15
