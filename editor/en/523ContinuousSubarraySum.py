from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cursum = 0
        pmodsums = {}
        for i, num in enumerate(nums):
            cursum += num
            key = cursum % k
            if not key and i >= 1:
                return True
            elif key in pmodsums:
                if i - pmodsums[key] > 1:
                    return True
            else:
                pmodsums[key] = i
        return False


assert Solution().checkSubarraySum([0, 0], 1) == True
assert Solution().checkSubarraySum([23, 2, 4, 6, 6], 7) == True
assert Solution().checkSubarraySum([23, 2, 4, 6, 7], 6) == True
