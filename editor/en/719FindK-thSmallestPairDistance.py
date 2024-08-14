from typing import List
from heapq import heapify, heappop, heappush, heapreplace


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapify(self.heap)
        # only k elements necessary
        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        # adding when not enough
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        # or replacing heap's head
        elif self.heap[0] < val:
            heapreplace(self.heap, val)
        # always heap's head -> kth largest
        return self.heap[0]


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        diffs = [-abs(nums[i] - nums[i + 1]) for i in range(n - 1)]
        obj = KthLargest(k, diffs)

        i = 0
        while len(obj.heap) < k and i < n:
            for j in range(n - i - 2):
                obj.add(-abs(nums[j] - nums[j + i + 2]))
            i += 1

        return -obj.heap[0]


assert Solution().smallestDistancePair([9, 10, 7, 10, 6, 1, 5, 4, 9, 8], 18) == 2
assert Solution().smallestDistancePair([1, 6, 1], 3) == 5
