from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(
            currentIndex: int, remainingTarget: int, currentPath: List[int]
        ) -> None:
            if remainingTarget < 0 or len(candidates) - 1 < currentIndex:
                return
            elif not remainingTarget:
                result.append(currentPath)
                return

            dfs(currentIndex + 1, remainingTarget, currentPath)
            dfs(
                currentIndex,
                remainingTarget - candidates[currentIndex],
                currentPath + [candidates[currentIndex]],
            )

        dfs(0, target, [])

        return result


assert Solution().combinationSum(candidates=[2, 3, 5], target=8) == [
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5],
]
