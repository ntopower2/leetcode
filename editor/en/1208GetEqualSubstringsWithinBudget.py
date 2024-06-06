import string


class Solution:
    def equalSubstring(self, s, t, cost):
        ltr = {c: i for i, c in enumerate(string.ascii_lowercase)}

        def diff(c1, c2):
            return abs(ltr[c1] - ltr[c2])

        j = 0
        for i, v in enumerate(zip(s, t)):
            sc, tc = v
            cost -= diff(sc, tc)
            if cost < 0:
                cost += diff(s[j], t[j])
                j += 1
        return i - j + 1


assert Solution().equalSubstring("krrgw", "zjxss", 19) == 2
assert Solution().equalSubstring("abzabc", "bcdbcd", 3) == 3
assert Solution().equalSubstring("abcd", "cdef", 3) == 1
