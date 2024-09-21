#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1
        for _ in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while not cur % 10:
                    cur //= 10
        return res


# @lc code=end

assert Solution().lexicalOrder(21) == [
    1,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    2,
    20,
    21,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
]
