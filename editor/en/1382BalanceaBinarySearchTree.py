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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodesSorted = []

        def dfs(s):
            if not s:
                return
            dfs(s.left)
            nodesSorted.append(s.val)
            dfs(s.right)
            return

        def createBalancedBSTFromSorted(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nodesSorted[mid])
            root.left = createBalancedBSTFromSorted(start, mid - 1)
            root.right = createBalancedBSTFromSorted(mid + 1, end)
            return root

        dfs(root)
        return createBalancedBSTFromSorted(0, len(nodesSorted) - 1)


tr1 = createTreeFrom([2, 1, 3])
