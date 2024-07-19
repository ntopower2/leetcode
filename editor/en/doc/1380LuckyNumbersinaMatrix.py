from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = set()
        maxs = [0] * len(matrix[0])
        for i, row in enumerate(matrix):
            mins.add(min(row))
            for j, col in enumerate(matrix[i]):
                maxs[j] = max(maxs[j], col)

        return [num for num in maxs if num in mins]


assert Solution().luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]) == [12]
