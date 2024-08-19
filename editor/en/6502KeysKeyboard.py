from math import inf, sqrt


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float(inf)] * n
        dp[0] = 0
        for i in range(2, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                if not i % j:
                    dp[i - 1] = min(dp[i - 1], dp[j - 1] + (i // j), dp[i // j - 1] + j)

        return dp[-1]


assert Solution().minSteps(6) == 5
assert Solution().minSteps(24) == 9
