from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hStack = []
        n = len(heights)
        largestArea = 0
        lefts = [0] * n
        rights = [n] * n
        for i in range(n):
            height = heights[i]
            while hStack != [] and heights[hStack[-1]] > height:
                rights[hStack[-1]] = i
                hStack.pop()
            lefts[i] = 0 if hStack == [] else hStack[-1] + 1
            hStack.append(i)

        for i in range(n):
            largestArea = max(largestArea, heights[i] * (rights[i] - lefts[i]))
        return largestArea


heights = [2, 1, 5, 6, 2, 3]
s = Solution().largestRectangleArea(heights)
