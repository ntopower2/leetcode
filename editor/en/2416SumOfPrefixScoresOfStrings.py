#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#

# @lc code=start
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.count = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        res = []

        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.count += 1

        for word in words:
            node = root
            tmp = 0
            for c in word:
                if c not in node.children:
                    break
                node = node.children[c]
                tmp += node.count
            res.append(tmp)

        return res


# @lc code=end

assert Solution().sumPrefixScores(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]
