from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        tmp = Counter(hand)
        x = min(tmp)
        cap = groupSize
        while len(tmp):
            while cap and tmp[x]:
                tmp[x] -= 1
                if not tmp[x]:
                    tmp.pop(x)
                cap -= 1
                x += 1
            if cap > 0:
                return False
            if not len(tmp):
                return True
            x = min(tmp)
            cap = groupSize

        return True


assert Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) == True
assert Solution().isNStraightHand([1, 2, 3, 4, 5], 4) == False
