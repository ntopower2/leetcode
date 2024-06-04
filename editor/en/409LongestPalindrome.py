from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = Counter(s)
        res = 0
        foundOne = False
        for freq in freqs.values():
            if not freq % 2:
                res += freq
            else:
                res += freq if not foundOne else freq - 1
                foundOne = True
        return res


assert Solution().longestPalindrome("bananas") == 5
assert Solution().longestPalindrome("abccccdd") == 7
assert Solution().longestPalindrome("a") == 1
