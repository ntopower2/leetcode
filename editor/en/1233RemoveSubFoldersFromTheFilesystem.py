#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        prev = None
        folder.sort()

        for path in folder:
            if not prev or not path.startswith(prev + "/"):
                res.append(path)
                prev = path

        return res


# @lc code=end
assert Solution().removeSubfolders(["/a", "/a/b/c", "/a/b/d"]) == ["/a"]
assert Solution().removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]) == [
    "/a",
    "/c/d",
    "/c/f",
]
