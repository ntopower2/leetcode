#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#


# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        mid = 1 << (n - 1)

        if k == mid:
            return "1"

        if k < mid:
            return self.findKthBit(n - 1, k)
        else:
            return "0" if self.findKthBit(n - 1, 2 * mid - k) == "1" else "1"


# @lc code=end


assert Solution().findKthBit(4, 11) == "1"
