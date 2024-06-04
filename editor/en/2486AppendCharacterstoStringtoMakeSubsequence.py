class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        cur = 0
        n = len(t)
        for c in s:
            if cur == len(t):
                return 0
            if t[cur] == c:
                cur += 1
        return n - cur


assert Solution().appendCharacters("coaching", "coding") == 4
assert Solution().appendCharacters("abcde", "a") == 0
