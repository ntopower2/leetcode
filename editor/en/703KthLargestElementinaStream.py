from heapq import heapify, heappush, heappop, heapreplace
from typing import List


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
    def kthLargest(self, arr: List):
        k, nums = arr[0]
        obj = KthLargest(k, nums)
        res = []
        for num in arr[1:]:
            res.append(obj.add(num[0]))
        return res


assert Solution().kthLargest([[2, [0]], [-1], [1], [-2], [-4], [3]]) == [-1, 0, 0, 0, 1]
