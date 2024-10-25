#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        tmp = None
        folder.sort()
        root = TrieNode()

        for path in folder:
            parts = path.split("/")[1:]
            cur = root

            for i, part in enumerate(parts):
                if part not in cur.children:
                    cur.children[part] = TrieNode()
                cur = cur.children[part]
                if cur.end:
                    tmp = i

            if tmp is None or tmp == len(parts) - 1:
                res.append(path)

            cur.end = True
            tmp = None

        return res


# @lc code=end
assert Solution().removeSubfolders(["/ah/al/am", "/ah/al"]) == ["/ah/al"]
assert Solution().removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]) == [
    "/a",
    "/c/d",
    "/c/f",
]
