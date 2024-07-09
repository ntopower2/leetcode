from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        meantime = current = 0
        for arrival, preparation in customers:
            if current < arrival:
                current += arrival - current
            current += preparation
            meantime += (current - arrival) / len(customers)

        return meantime


assert Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]) == 5.0
assert Solution().averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]) == 3.25
