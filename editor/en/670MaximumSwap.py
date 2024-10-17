#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#


# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        lst = list(str(num))
        M = (-1, -1)
        l, r = -1, -1
        for i in range(len(lst) - 1, -1, -1):
            d = int(lst[i])
            if M[0] < d:
                M = (d, i)
            elif d < M[0]:
                l = i
                r = M[1]

        if l != -1:
            lst[l], lst[r] = lst[r], lst[l]

        return int("".join(lst))


# @lc code=end
assert Solution().maximumSwap(98368) == 98863
