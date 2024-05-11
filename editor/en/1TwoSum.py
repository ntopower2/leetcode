from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, v in enumerate(nums):
            if v in numDict.keys():
                return [numDict[v], i]
            numDict[target - v] = i
        return None


assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
