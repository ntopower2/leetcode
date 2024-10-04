#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        cSkill = Counter(skill)
        target = sum(skill) * 2
        if not target % len(skill):
            target //= len(skill)
        else:
            return -1
        for s in cSkill:
            if s > target / 2:
                continue
            if target - s == s:
                if cSkill[s] % 2:
                    return -1
                res += s * s * cSkill[s] // 2
            else:
                if cSkill[s] == cSkill[target - s]:
                    res += s * (target - s) * cSkill[s]
                else:
                    return -1

        return res


# @lc code=end
assert Solution().dividePlayers([4, 4, 2, 4, 4, 5]) == -1
assert Solution().dividePlayers([3, 2, 5, 1, 3, 4]) == 22
