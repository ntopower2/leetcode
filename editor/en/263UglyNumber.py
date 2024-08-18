class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for prime in [2, 3, 5]:
            while not num % prime:
                num //= prime
        return num == 1
