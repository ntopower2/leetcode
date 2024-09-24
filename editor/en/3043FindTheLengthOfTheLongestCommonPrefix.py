#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            return self.longestCommonPrefix(arr2, arr1)

        root = TrieNode()
        for word in arr1:
            node = root
            for c in str(word):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isWord = True

        res = tmp = 0
        for word in arr2:
            node = root
            for c in str(word):
                if c not in node.children:
                    break
                node = node.children[c]
                tmp += 1

            res = max(res, tmp)
            tmp = 0

        return res


# @lc code=end

assert Solution().longestCommonPrefix(arr1=[1, 2, 3], arr2=[4, 2, 4]) == 1
