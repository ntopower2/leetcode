from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        tmp = mean * (n + m) - sum(rolls)
        div, mod = divmod(tmp, n)
        if div > 6 or div <= 0:
            return []
        res = [div] * n
        for i in range(mod):
            if res[i] == 6:
                return []
            res[i] += 1
        return res


assert Solution().missingRolls(rolls=[1, 5, 6], mean=3, n=4) == [3, 2, 2, 2]
