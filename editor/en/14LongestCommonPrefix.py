from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = min(strs, key=len)

        for s in strs:
            if not res:
                return res
            tmp = ""
            for c1, c2 in zip(res, s):
                if c1 != c2:
                    break
                tmp += c1
            res = tmp

        return res


assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
