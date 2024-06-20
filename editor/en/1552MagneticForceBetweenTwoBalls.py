from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        if m == 2:
            return max(position) - min(position)

        position.sort()
        l, r = 1, position[-1] - position[0]

        if m == len(position):
            return min([position[i + 1] - position[i] for i in range(m - 1)])

        def canPlaceFor(targetForce):
            tmpM = m - 1
            start = position[0]
            for end in position[1:]:
                if end - start >= targetForce:
                    start = end
                    tmpM -= 1
                if not tmpM:
                    break
            return not tmpM

        while l < r:
            mid = (l + r + 1) // 2
            if canPlaceFor(mid):
                l = mid
            else:
                r = mid - 1
        return l


assert Solution().maxDistance([79, 74, 57, 22], 4) == 5
assert Solution().maxDistance([1, 2, 3, 4, 7], 3) == 3
assert Solution().maxDistance([5, 4, 3, 2, 1, 1000000000], 2) == 999999999
