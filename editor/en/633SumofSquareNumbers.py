from math import floor, sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, floor(sqrt(c))
        while i <= j:
            tmp = i * i + j * j
            if c < tmp:
                j -= 1
            elif c > tmp:
                i += 1
            else:
                return True
        return False


assert Solution().judgeSquareSum(2) == True
assert Solution().judgeSquareSum(0) == True
assert Solution().judgeSquareSum(5) == True
assert Solution().judgeSquareSum(3) == False
assert Solution().judgeSquareSum(9) == True
