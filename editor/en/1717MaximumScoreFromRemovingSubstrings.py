class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        checkForABstack = []
        res = 0
        if y > x:
            return self.maximumGain(s[::-1], y, x)

        for c in s:
            if c == "b" and checkForABstack and checkForABstack[-1] == "a":
                res += x
                checkForABstack.pop()
            else:
                checkForABstack.append(c)

        checkForBAstack = []
        while checkForABstack:
            c = checkForABstack.pop()
            if c == "b" and checkForBAstack and checkForBAstack[-1] == "a":
                res += y
                checkForBAstack.pop()
            else:
                checkForBAstack.append(c)

        return res


assert (
    Solution().maximumGain(
        "aabbabkbbbfvybssbtaobaaaabataaadabbbmakgabbaoapbbbbobaabvqhbbzbbkapabaavbbeghacabamdpaaqbqabbjbababmbakbaabajabasaabbwabrbbaabbafubayaazbbbaababbaaha",
        1926,
        4320,
    )
    == 19
)
assert Solution().maximumGain("cdbcbbaaabab", 4, 5) == 19
assert Solution().maximumGain("aabbaaxybbaabb", 5, 4) == 20
