#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#


# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        unq1, unq2 = Counter(s1.split(" ")), Counter(s2.split(" "))
        unq1 += unq2
        res = []
        for word in unq1:
            if unq1[word] == 1:
                res.append(word)
        return res


# @lc code=end

assert Solution().uncommonFromSentences("fo ly ly", "fo fo etx") == ["etx"]
