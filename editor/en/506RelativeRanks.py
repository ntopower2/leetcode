from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexToScore = []
        for i, val in enumerate(score):
            indexToScore.append((val, i))
        indexToScore.sort(reverse=True)
        for i, tup in enumerate(indexToScore):
            if i == 0:
                score[indexToScore[0][1]] = "Gold Medal"
            elif i == 1:
                score[indexToScore[1][1]] = "Silver Medal"
            elif i == 2:
                score[indexToScore[2][1]] = "Bronze Medal"
            else:
                score[tup[1]] = str(i + 1)

        return score


assert Solution().findRelativeRanks([10, 3, 8, 9, 4]) == [
    "Gold Medal",
    "5",
    "Bronze Medal",
    "Silver Medal",
    "4",
]
