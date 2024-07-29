from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total_teams = 0

        for j in range(1, n - 1):
            left_smaller = left_larger = right_smaller = right_larger = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_larger += 1

            total_teams += left_smaller * right_larger
            total_teams += left_larger * right_smaller

        return total_teams


assert Solution().numTeams([2, 5, 3, 4, 1]) == 3
