class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        tmp = 0
        for i in range(1, n + 1):
            tmp += k
            tmp %= i

        return tmp + 1


assert Solution().findTheWinner(5, 2) == 3
assert Solution().findTheWinner(6, 5) == 1
