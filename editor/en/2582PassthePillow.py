class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        routes, remainder = divmod(time, n - 1)
        return n - remainder if routes % 2 else remainder + 1


assert Solution().passThePillow(9, 4) == 5
assert Solution().passThePillow(3, 2) == 3
assert Solution().passThePillow(4, 5) == 2
