from typing import List
from math import log10, ceil


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def countSort(nums: List[int], power: int):
            out = [0] * len(nums)
            counts = [0] * 10
            for num in nums:
                counts[(num // power % 10)] += 1

            for i in range(1, 10):
                counts[i] += counts[i - 1]

            for num in nums[::-1]:
                tmp = num // power % 10
                out[counts[tmp] - 1] = num
                counts[tmp] -= 1

            for i in range(len(nums)):
                nums[i] = out[i]

        if len(nums) == 1:
            return nums

        M = max(nums)
        m = min(nums)
        size = ceil(log10(M)) + 1

        if m < 0:
            neg = []
            pos = []
            for num in nums:
                if num < 0:
                    neg.append(-num)
                else:
                    pos.append(num)
            sizeN = ceil(log10(-m)) + 1
            for i in range(size):
                countSort(pos, 10**i)
            for i in range(sizeN):
                countSort(neg, 10**i)
            nums[: len(neg)] = map(lambda x: -x, neg[::-1])
            nums[len(neg) :] = pos
        else:
            for i in range(size):
                countSort(nums, 10**i)
        return nums


assert Solution().sortArray([-1, 2, -8, -10]) == [-10, -8, -1, 2]
assert Solution().sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
assert Solution().sortArray([18, 154, 31, 58]) == [18, 31, 58, 154]
