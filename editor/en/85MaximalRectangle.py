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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        largestArea = 0
        currentHist = [0] * len(matrix[0])
        for row in matrix:
            currentHist = [(a + 1) * int(b) for a, b in zip(currentHist, row)]
            largestArea = max(largestArea, self.largestRectangleArea(currentHist))
        return largestArea


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
s = Solution().maximalRectangle(matrix)
