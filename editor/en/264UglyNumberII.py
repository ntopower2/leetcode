class Solution:
    def nthUglyNumber(self, n: int) -> int:
        next = [[2, 0, 2], [3, 0, 3], [5, 0, 5]]
        nums = [1] * n

        for i in range(1, n):
            ugly = [0, next[0][-1]]
            for j, val in enumerate(next):
                if val[-1] < ugly[-1]:
                    ugly = [j, val[-1]]

            nums[i] = ugly[1]
            for j, val in enumerate(next):
                if ugly[1] == val[2]:
                    val[1] += 1
                    val[2] = nums[val[1]] * val[0]

        return nums[-1]


assert Solution().nthUglyNumber(10) == 12
assert Solution().nthUglyNumber(11) == 15
assert Solution().nthUglyNumber(458) == 600000
