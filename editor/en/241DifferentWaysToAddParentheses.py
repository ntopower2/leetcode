#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

from typing import List
import re

# @lc code=start


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        exp = re.compile("(\d+)([\+\-\*\/])?")
        parts = exp.findall(expression)
        nums, ops = [], []
        for num, op in parts:
            nums.append(int(num))
            if op:
                ops.append(op)

        memo = {}

        def compute(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            if start == end:
                return [nums[start]]

            results = []
            for i in range(start, end):
                left = compute(start, i)
                right = compute(i + 1, end)

                for l in left:
                    for r in right:
                        if ops[i] == "+":
                            results.append(l + r)
                        elif ops[i] == "-":
                            results.append(l - r)
                        else:  # ops[i] == '*'
                            results.append(l * r)

            memo[(start, end)] = results
            return results

        return compute(0, len(nums) - 1)


# @lc code=end

assert Solution().diffWaysToCompute("2*3-4*5") == [-34, -14, -10, -10, 10]
