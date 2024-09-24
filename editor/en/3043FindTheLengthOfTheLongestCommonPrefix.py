#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            return self.longestCommonPrefix(arr2, arr1)

        prefixes = set()
        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10

        res = 0
        for num in arr2:
            while num and num not in prefixes:
                num //= 10
            if num in prefixes:
                res = max(res, len(str(num)))

        return res


# @lc code=end

assert Solution().longestCommonPrefix(arr1=[1, 2, 3], arr2=[4, 2, 4]) == 1
