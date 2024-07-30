class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = len(s)
        before = [0] * (len(s) + 1)
        count = 0
        for i in range(len(s)):
            before[i + 1] = before[i] + (s[i] == "b")
            count += s[i] == "a"

        for i in range(len(s)):
            count -= s[i] == "a"
            res = min(res, count + before[i])

        return res


assert Solution().minimumDeletions("aababbab") == 2
