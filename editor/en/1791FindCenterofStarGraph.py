from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        if edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            return edges[0][1]
        return 0


assert Solution().findCenter([[1, 2], [2, 3], [4, 2]]) == 2
