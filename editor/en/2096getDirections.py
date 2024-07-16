from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (
            self
            and other
            and self.val == other.val
            and self.left.__eq__(other.left)
            and self.right.__eq__(other.right)
        )


def createTreeFrom(nodes: List[int]) -> TreeNode:
    treeNodes = [None] * len(nodes)
    treeNodes[0] = TreeNode(nodes[0])
    for i, node in enumerate(nodes):
        if node is not None and i > 0:
            treeNodes[i] = TreeNode(node)
            if i % 2:
                treeNodes[(i - 1) // 2].left = treeNodes[i]
            else:
                treeNodes[(i - 1) // 2].right = treeNodes[i]

    return treeNodes


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        pathToStart = []
        pathToDest = []
        res = ""
        if startValue == destValue:
            return res

        def findDest(s, t, path: List[int]):
            if not s:
                return False
            path.append(s)
            if s.val == t:
                return True

            if (s.left and findDest(s.left, t, path)) or (
                s.right and findDest(s.right, t, path)
            ):
                return True

            path.pop()
            return False

        findDest(root, startValue, pathToStart)
        findDest(root, destValue, pathToDest)

        i = 0
        while (
            i < min(len(pathToStart), len(pathToDest))
            and pathToStart[i].val == pathToDest[i].val
        ):
            i += 1

        lca = pathToStart[i - 1]
        j = 1
        while pathToStart[-j].val != lca.val:
            j += 1
            res += "U"

        for j in range(i - 1, len(pathToDest) - 1):
            if pathToDest[j].left and pathToDest[j].left.val == pathToDest[j + 1].val:
                res += "L"
            else:
                res += "R"

        return res


tr1 = createTreeFrom([5, 1, 2, 3, None, 6, 4])
assert Solution().getDirections(createTreeFrom([2, 1])[0], 2, 1) == "L"
assert Solution().getDirections(tr1[0], 3, 6) == "UURL"
