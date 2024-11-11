#
# @lc app=leetcode id=2601 lang=python3
#
# [2601] Prime Subtraction Operation
#

# @lc code=start
from typing import List
from bisect import bisect_left


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieveOfEratosthenes(maxNum):
            isPrime = [True] * (maxNum + 1)
            p = 2
            while p * p <= maxNum:
                if isPrime[p]:
                    for i in range(p * p, maxNum + 1, p):
                        isPrime[i] = False
                p += 1
            primes = [p for p in range(2, maxNum + 1) if isPrime[p]]
            return primes

        if len(nums) == 1:
            return True

        primes = sieveOfEratosthenes(max(nums))

        def findCloserPrime(num):
            nonlocal primes
            index = bisect_left(primes, num)
            return primes[index - 1] if index else -1

        for i, num in enumerate(nums):
            p = findCloserPrime(num - nums[i - 1] if i > 0 else num)
            if p == -1:
                if i > 0 and nums[i - 1] >= num:
                    return False
                else:
                    continue
            nums[i] -= p

        return True


# @lc code=end
assert Solution().primeSubOperation([1, 20]) == True
assert Solution().primeSubOperation([5, 8, 3]) == False
