#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
from typing import List
class TimePoint:
    def __init__(self, objstr) -> None:
        hr, mn = map(int, objstr.split(":"))
        self.mn = mn + hr*60
    
    def __lt__(self, other):
        return self.mn < other.mn
    
    def __le__(self, other):
        return self.mn <= other.mn
    
    def __eq__(self, other: object) -> bool:
        return self.mn == other.mn
    
    def __hash__(self) -> int:
        return self.mn
    
    def __sub__(self, other):
        M = 1440
        if self.__le__(other):
            return min(other.mn-self.mn, M - other.mn + self.mn)
        else:
            return other.__sub__(self)
        


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        res = 1441
        n = len(timePoints)
        timePoints = sorted(set(map(TimePoint, timePoints)))
        if n != len(timePoints):
            return 0
        n = len(timePoints)
        for i in range(n-1):
            res = min(res, timePoints[i+1] - timePoints[i])
        return min(res, timePoints[n-1] - timePoints[0]) 
        
# @lc code=end

assert Solution().findMinDifference(["00:00","23:59","00:00"]) == 0
