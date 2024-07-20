from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0 for _ in colSum] for _ in rowSum]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                tmp = min(rowSum[i], colSum[j])
                res[i][j] = tmp
                colSum[j] -= tmp
                rowSum[i] -= tmp

        return res


assert Solution().restoreMatrix([3, 8], [4, 7]) == [[3, 0], [1, 7]]
