class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k -= 1
        s = list(range(n))
        i = 0

        while len(s) > 1:
            steps = 0
            if i == len(s):
                i = 0
            while steps < k:
                i += 1
                steps += 1
                if i == len(s):
                    i = 0
            s.pop(i)

        return s[0] + 1


assert Solution().findTheWinner(6, 5) == 1
