from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(
            currentIndex: int, remainingTarget: int, currentPath: List[int]
        ) -> None:
            if remainingTarget < 0:
                return
            elif not remainingTarget:
                result.append(currentPath)
                return

            for i, candidate in enumerate(
                candidates[currentIndex:], start=currentIndex
            ):
                if currentIndex < i and candidate == candidates[i - 1]:
                    continue
                if remainingTarget < candidate:
                    break
                dfs(i + 1, remainingTarget - candidate, currentPath + [candidate])

        dfs(0, target, [])

        return result


assert Solution().combinationSum2([3, 1, 3, 5, 1, 1], 8) == [
    [1, 1, 1, 5],
    [1, 1, 3, 3],
    [3, 5],
]
assert Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8) == [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6],
]
