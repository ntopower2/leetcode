class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def getIndexFrom(ltr: str) -> int:
            return ord(ltr) - 96

        def sumDigits(num: int) -> int:
            total = 0
            while num > 0:
                num, remainder = divmod(num, 10)
                total += remainder
            return total

        res = sum(map(sumDigits, map(getIndexFrom, s)))

        for _ in range(k - 1):
            res = sumDigits(res)

        return res


assert Solution().getLucky("iaozzbyqzwbpurzze", 2) == 5
assert Solution().getLucky("leetcode", 2) == 6
