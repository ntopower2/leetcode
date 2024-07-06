class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        routes, remainder = divmod(k, n)
        return n - remainder if routes % 2 else remainder


assert Solution().numberOfChild(3, 5) == 1
