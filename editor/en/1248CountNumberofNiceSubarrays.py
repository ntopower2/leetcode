from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k:
            return 1 if sum([num % 2 for num in nums]) == n else 0
        if not any([num for num in nums if num % 2]):
            return 0

        pref = [1]
        tmp = res = 0
        for i in range(n):
            if nums[i] % 2:
                tmp += 1
            if tmp >= k and len(pref) - 1 >= tmp - k:
                res += pref[tmp - k]
            if tmp > len(pref) - 1:
                pref.append(1)
            else:
                pref[tmp] += 1

        return res


assert Solution().numberOfSubarrays([1, 1, 1, 1, 1], 1) == 5
assert Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
