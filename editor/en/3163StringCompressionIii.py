#
# @lc app=leetcode id=3163 lang=python3
#
# [3163] String Compression III
#


# @lc code=start
class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        tmp = 1
        cur = word[0]
        for c in word[1:]:
            if cur != c or tmp == 9:
                res.append(str(tmp))
                res.append(cur)
                tmp = 1
                cur = c
            else:
                tmp += 1

        res.append(str(tmp))
        res.append(cur)

        return "".join(res)


# @lc code=end

assert Solution().compressedString("aaaa") == "4a"
assert Solution().compressedString("abcde") == "1a1b1c1d1e"
assert Solution().compressedString("aaaaaaaaaaaaaabb") == "9a5a2b"
