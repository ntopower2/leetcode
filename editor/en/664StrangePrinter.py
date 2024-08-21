from functools import lru_cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            res = dp(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    res = min(res, dp(i, k) + dp(k + 1, j - 1))

            return res

        return dp(0, n - 1)


assert Solution().strangePrinter("aaabbb") == 2
