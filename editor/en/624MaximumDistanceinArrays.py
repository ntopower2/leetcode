from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if arrays[0][0] < arrays[1][0]:
            mindiff = [arrays[0][0], abs(arrays[1][-1] - arrays[0][0])]
        else:
            mindiff = [arrays[1][0], abs(arrays[0][-1] - arrays[1][0])]

        if arrays[0][-1] < arrays[1][-1]:
            maxdiff = [arrays[1][-1], abs(arrays[1][-1] - arrays[0][0])]
        else:
            maxdiff = [arrays[0][-1], abs(arrays[0][-1] - arrays[1][0])]

        for arr in arrays[2:]:
            m, M = arr[0], arr[-1]
            mindiff[1] = max(mindiff[1], abs(M - mindiff[0]))
            mindiff[0] = min(mindiff[0], m)
            maxdiff[1] = max(maxdiff[1], abs(m - maxdiff[0]))
            maxdiff[0] = max(maxdiff[0], M)

        return max(mindiff[1], maxdiff[1])


assert Solution().maxDistance(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]) == 4
