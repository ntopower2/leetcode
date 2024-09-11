class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        l = max(len(start), len(goal))
        start = "0" * (l - len(start)) + start
        goal = "0" * (l - len(goal)) + goal

        return sum([i != j for i, j in zip(start, goal)])


assert Solution().minBitFlips(10, 7) == 3
