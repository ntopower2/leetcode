class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = bs = 0
        for c in s:
            if c == "b":
                bs += 1
            elif bs:
                res += 1
                bs -= 1
        return res


assert Solution().minimumDeletions("aababbab") == 2
