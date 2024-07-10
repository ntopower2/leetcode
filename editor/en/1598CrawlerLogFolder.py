from typing import List


class FNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.parent = parent


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        root = FNode("")
        cur = root
        for log in logs:
            if log == "../" and cur.parent:
                cur = cur.parent
            elif not log.startswith("."):
                foldername = log.split("/")[0]
                if foldername not in cur.children.keys():
                    folder = FNode(foldername, parent=cur)
                    cur.children[foldername] = folder
                cur = cur.children[foldername]
        i = 0
        while cur.parent:
            cur = cur.parent
            i += 1
        return i


assert Solution().minOperations(["d1/", "d2/", "../", "d21/", "./"]) == 2
