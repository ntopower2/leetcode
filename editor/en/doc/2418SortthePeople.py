from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        return [
            names[i]
            for i in sorted(range(len(heights)), key=lambda i: heights[i], reverse=True)
        ]


assert Solution().sortPeople(
    names=["Mary", "John", "Emma"], heights=[180, 165, 170]
) == ["Mary", "Emma", "John"]
