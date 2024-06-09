from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        tmp = 0
        pmodsums = {}
        for num in nums:
            tmp += num
            tmp %= k
            pmodsums[tmp] = pmodsums.get(tmp, 0) + 1
        tmp = 0
        for key, val in pmodsums.items():
            if not key:
                tmp += val
            tmp += (val - 1) * val // 2
        return tmp


assert Solution().subarraysDivByK([8, 9, 7, 8, 9], 8) == 7
assert Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5) == 7
