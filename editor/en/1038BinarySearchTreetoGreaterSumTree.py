from typing import List


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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def dfs(s):
            if not s:
                return
            dfs(s.right)
            self.total += s.val
            s.val = self.total
            dfs(s.left)
            return

        dfs(root)
        return root


tr1 = createTreeFrom([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
tr2 = createTreeFrom(
    [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
)
assert Solution().bstToGst(tr1[0]) == tr2[0]
