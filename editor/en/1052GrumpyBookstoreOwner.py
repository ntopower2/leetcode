from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        if max(grumpy) == 0:
            return sum(customers)
        windowBenefit = tmp = i = 0
        n = len(customers)

        while not grumpy[i]:
            tmp += customers[i]
            i += 1
        tmp += sum(customers[i : min(n, i + minutes)])
        if i + minutes < n:
            tmp += sum([customers[j] for j in range(i + minutes, n) if not grumpy[j]])
        windowBenefit = tmp

        for j in range(i + 1, n - minutes + 1):
            if grumpy[j - 1]:
                tmp -= customers[j - 1]
            windowStop = j + minutes - 1
            if windowStop < n and grumpy[windowStop]:
                tmp += customers[windowStop]
            if tmp > windowBenefit:
                windowBenefit = tmp

        return windowBenefit


assert (
    Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16
)
assert Solution().maxSatisfied([4, 10, 10], [1, 1, 0], 2) == 24
