from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0, 0]
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                if not change[0]:
                    return False
                change[1] += 1
                change[0] -= 1
            else:
                if not (change[1] and change[0]) and change[0] < 3:
                    return False
                change[0] -= 1
                if change[1]:
                    change[1] -= 1
                else:
                    change[0] -= 2
        return True


assert Solution().lemonadeChange([5, 5, 5, 5, 10, 5, 10, 10, 10, 20]) == True
assert Solution().lemonadeChange([5, 5, 10, 10, 20]) == False
