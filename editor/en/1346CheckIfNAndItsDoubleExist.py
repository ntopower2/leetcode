#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        targets = set()
        for num in arr:
            if (not (num % 2) and num / 2 in targets) or 2 * num in targets:
                return True
            targets.add(num)
        return False


# @lc code=end

assert Solution().checkIfExist([10, 2, 5, 3]) == True
