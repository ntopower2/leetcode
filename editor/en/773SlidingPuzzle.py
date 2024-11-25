#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def produceNextStates(state: List[int]) -> List[List[int]]:
            zeroPos = state.index(0)
            states = []
            if zeroPos == -1:
                raise ValueError("Incorrect State")
            tmp = state.copy()

            tmp[zeroPos % 3 + 3], tmp[zeroPos % 3] = (
                tmp[zeroPos % 3],
                tmp[zeroPos % 3 + 3],
            )
            states.append(tmp)

            if zeroPos not in (2, 5):
                tmp = state.copy()
                tmp[zeroPos + 1], tmp[zeroPos] = tmp[zeroPos], tmp[zeroPos + 1]
                states.append(tmp)
            if zeroPos not in (0, 3):
                tmp = state.copy()
                tmp[zeroPos - 1], tmp[zeroPos] = tmp[zeroPos], tmp[zeroPos - 1]
                states.append(tmp)

            return states

        goal = [1, 2, 3, 4, 5, 0]
        state = board[0] + board[1]
        if goal == state:
            return 0

        visited = set()
        q = deque([state])
        visited.add(tuple(state))
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                states = produceNextStates(cur)
                if goal in states:
                    return res
                for state in states:
                    t = tuple(state)
                    if t not in visited:
                        visited.add(t)
                        q.append(state)

        return -1


# @lc code=end

assert Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]) == 5
