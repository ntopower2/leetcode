from collections import defaultdict
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = i = 0
        curBoatWeight = 0
        j = len(people) - 1
        flag = False
        people.sort()

        while i <= j:
            if people[j] <= limit:
                boats += 1
                curBoatWeight = people[j]
                flag = True
            if people[i] + curBoatWeight <= limit and i < j:
                curBoatWeight += people[i]
                i += 1
            if flag:
                j -= 1
                flag = False
        return boats


assert (
    Solution().numRescueBoats(
        [2, 2, 2, 6, 6, 7, 10, 10, 10, 11, 12, 13, 18, 22, 26, 33, 41, 47, 49, 50], 50
    )
    == 11
)
assert Solution().numRescueBoats([2, 2], 6) == 1
assert Solution().numRescueBoats([3, 3, 4, 5], 5) == 4
assert Solution().numRescueBoats([1, 2], 3) == 1
