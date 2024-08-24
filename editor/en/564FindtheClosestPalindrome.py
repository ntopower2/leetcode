from math import ceil


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def createPalindrome(prefix: str, L: int):
            if L % 2:
                return prefix + prefix[-2::-1]
            return prefix + prefix[::-1]

        def isPalindrome(n: str):
            L = len(n)
            for i in range(ceil(L / 2)):
                if n[i] != n[L - i - 1]:
                    return False
            return True

        L = len(n)
        if L == 1:
            return str(int(n) - 1)

        nearest = set(
            [
                "9" * L,
                "9" * (L - 1),
                "1" + "0" * (L - 1) + "1",
                "1" + "0" * (L - 2) + "1",
            ]
        )
        choices = [-1, 0, 1] if not isPalindrome(n) else [-1, 1]
        prefix = n[: (L + 1) // 2]

        for choice in choices:
            prefixWithChoice = str(int(prefix) + choice)
            nearest.add(createPalindrome(prefixWithChoice, L))

        nearest.discard(n)

        closest = min(nearest, key=lambda x: (abs(int(x) - int(n)), int(x)))
        return closest


assert Solution().nearestPalindromic("11") == "9"
assert Solution().nearestPalindromic("121") == "111"
